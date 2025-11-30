<script lang="ts">
	import Loader from "./Loader.svelte";
	import SummaryView from "./SummaryView.svelte";

    let files: FileList | undefined = $state();
    let status: "Idle" | "Working" = $state("Idle")

    function onclick() {
        status = status === "Idle" ? "Working" : "Idle"
    }
</script>

<h1 class="hero idle">Transforme Voz em Texto</h1>

<form onsubmit={onclick}>
    <label for="file">Upload a audio file:</label>
    <input accept="audio/*" bind:files id="file" name="file" type="file" />
    <button>Generate Summary</button>
</form>

{#if status === "Idle"}
    <Loader />
{:else if status === "Working"}
    <SummaryView />
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