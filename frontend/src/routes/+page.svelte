<script lang="ts">
	import Loader from "../lib/components/Loader.svelte";
	import SummaryView from "../lib/components/SummaryView.svelte";
    import Hero from "../lib/components/Hero.svelte";
    import UploadForm from "../lib/components/UploadForm.svelte";

    let files: FileList | undefined = $state();

    let status: "Idle" | "Processing" | "Done" = $state("Idle");
    let summaryResult: string = $state("");

    // async function onsubmit(event: Event) {
    //     event.preventDefault();

    //     if (!files || files.length === 0) {
    //         alert("Por favor, selecione um arquivo de áudio para upload.");
    //         return;
    //     }
    //     status = "Processing";

    //     const formData = new FormData();
    //     formData.append("myFile", files[0]);

    //     try {
    //         const response = await fetch("/api/process-audio", {
    //             method: "POST",
    //             body: formData
    //         });

    //         if (!response.ok) {
    //             throw new Error("Erro ao processar o arquivo de áudio.");
    //         }

    //         const { id } = await response.json();

    //         // Polling for result
    //         const interval = setInterval(async () => {
    //             try {
    //                 const resultResponse = await fetch(`/api/get-summary/${id}`);
    //                 const data = await resultResponse.json();

    //                 if (data.state === "SUCCESS") {
    //                     clearInterval(interval);
    //                     summaryResult = data.result.summary;
    //                     status = "Done";
                    
    //                 } else if (data.state === "FAILURE" || data.state === "REVOKED") {
    //                     clearInterval(interval);
    //                     alert("Falha ao processar o áudio.");
    //                     status = "Idle";
    //                 }
    //             } catch (error) {
    //                 clearInterval(interval);
    //                 console.error(error);
    //                 status = "Idle";
    //             }
    //         }, 2000);

    //     } catch (error) {
    //         console.error(error);
    //         alert("Erro ao conectar com o servidor.");
    //         status = "Idle";
    //     }
    // }

    async function onsubmit(event: Event) {
        event.preventDefault();

        status = "Processing";
        setTimeout(() => {
            summaryResult = "# Topico 1\n\n ## Subtop 1\n\n ### Detalhe 1\n\n # Topico 2\n\n";
            status = "Done";
        }, 3000);
    }
</script>

{#if status !== "Done"}
    <Hero />
{/if}

<UploadForm {status} bind:files {onsubmit} />

{#if status === "Processing"}
    <Loader />
{:else if status === "Done"}
    <SummaryView summary={summaryResult} />
{/if}