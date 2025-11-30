<script lang="ts">
	import Loader from "./Loader.svelte";
	import SummaryView from "./SummaryView.svelte";

    let files: FileList | undefined = $state();

    let status: "Idle" | "Processing" | "Done" = $state("Idle");
    let summaryResult: string = $state("");

    async function handleSubmit(event: Event) {
        event.preventDefault();

        if (!files || files.length === 0) {
            alert("Por favor, selecione um arquivo de áudio para upload.");
            return;
        }
        status = "Processing";

        const formData = new FormData();
        formData.append("myFile", files[0]);

        try {
            const response = await fetch("/api/process-audio", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error("Erro ao processar o arquivo de áudio.");
            }

            const { id } = await response.json();

            // Polling for result
            const interval = setInterval(async () => {
                try {
                    const resultResponse = await fetch(`/api/get-summary/${id}`);
                    const data = await resultResponse.json();

                    if (data.state === "SUCCESS") {
                        clearInterval(interval);
                        summaryResult = data.result.summary;
                        status = "Done";
                    
                    } else if (data.state === "FAILURE" || data.state === "REVOKED") {
                        clearInterval(interval);
                        alert("Falha ao processar o áudio.");
                        status = "Idle";
                    }
                } catch (error) {
                    clearInterval(interval);
                    console.error(error);
                    status = "Idle";
                }
            }, 2000);

        } catch (error) {
            console.error(error);
            alert("Erro ao conectar com o servidor.");
            status = "Idle";
        }
    }
</script>

<h1 class="hero idle">Transforme Voz em Texto</h1>

<form onsubmit={handleSubmit}>
    <label for="file">Upload a audio file:</label>
    <input accept="audio/*" bind:files id="file" name="file" type="file" />
    <button type="submit" disabled={status === "Processing"}>
        {status === "Processing" ? "Processando..." : "Gerar Resumo"}
    </button>
</form>


{#if status === "Processing"}
    <Loader />
{:else if status === "Done"}
    <SummaryView summary={summaryResult} />
{/if}


<style>

:global(body) {
    background: var(--color-background-dark);
    color : var(--color-text-dark);
    font-family: var(--font-family-body);
    margin: 20px;
}

h1.hero {
    font-size: 3rem;
    text-align: center;
    margin-bottom: 2rem;
}



</style>