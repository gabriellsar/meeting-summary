<script lang="ts">
    let {
        status,
        files=$bindable(),
        onsubmit
    } = $props();

    const formElements = [
        {id: "form"},
    ]
</script> 

{#each formElements as element (element.id) }
<form {onsubmit} class="upload-section" class:compact={status === "Done"}>

    <div class="file-input-wrapper">
        <label for="file" class="file-label">
            <div class="content">
                <i class="fa-solid fa-cloud-arrow-up icon"></i>
                <span class="filename">
                    {#if files && files.length > 0}
                        {files[0].name}
                    {:else}
                        {#if status === "Done"}
                            Carregar outro arquivo
                        {:else}
                            Escolha um arquivo ou arraste aqui
                        {/if}
                    {/if}
                </span>
            </div>
        </label>
        <input class="hidden-input" accept="audio/*" bind:files id="file" name="file" type="file" />
    </div>
       
    <button type="submit" disabled={status === "Processing"} class="submit-btn">
        {#if status === "Idle"}
            Gerar Resumo
        {:else if status === "Processing"}
            Processando...
        {:else if status === "Done"}
            <i class="fa-solid fa-share"></i>
        {/if}
    </button>
        
</form>
{/each}

<style>
@property --gradient-angle {
    syntax: "<angle>";
    inherits: false;
    initial-value: 0deg;
}

.upload-section {
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 1.5rem;
    margin-bottom: 2rem;

}

.hidden-input {
    position: absolute;
    width: 100%;
    height: 100%;
    top: 0;
    left: 0;
    opacity: 0;
    cursor: pointer;
}

.file-input-wrapper {
    position: relative;
    width: 100%;
    max-width: 500px;
    height: 80px;
    border-radius: 12px;
    cursor: pointer;

}

.file-input-wrapper::before {
    content: "";
    position: absolute;
    inset: -3px; 
    background: conic-gradient(
        from var(--gradient-angle), 
        var(--color-primary-dark), 
        var(--color-secondary-dark), 
        var(--color-primary-dark)
    );
    border-radius: 14px; 
    z-index: -1;
    animation: spin 5s linear infinite;
}

.file-label {
    width: 100%;
    height: 100%;
    background: var(--color-background-dark);
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    transition: background-color 0.3s;
}

.content {
    display: flex;
    align-items: center;
    gap: 1rem;
    color: var(--color-text-dark);
    font-family: var(--font-family-body);
}

.icon {
    font-size: 1.5rem;
    color: var(--color-primary-dark);
}

.filename {
    font-size: 1rem;
    opacity: 0.9;
}

.submit-btn {
    background: linear-gradient(135deg, var(--color-secondary-dark), var(--color-accent-dark));
    color: white;
    border: none;
    padding: 0.8rem 2rem;
    border-radius: 8px;
    font-weight: 600;
    cursor: pointer;
    transition: opacity 0.2s, transform 0.1s;
}

.submit-btn:disabled {
    opacity: 0.5;
    cursor: not-allowed;
}

.submit-btn:hover:not(:disabled) {
    opacity: 0.9;
}

@keyframes spin {
    from {--gradient-angle: 0deg;}
    to {--gradient-angle: 360deg;}
}


.upload-section.compact {
    flex-direction: row;
    justify-content: end;
    gap: 1rem;
    margin-bottom: 1rem;
    padding: 1rem;
    
    border-radius: 8px;
}

.upload-section.compact .file-input-wrapper {
    height: 40px;
    max-width: 300px;
}

.upload-section.compact .file-label .content {
    font-size: 0.85rem;
    gap: 0.5rem;
}

.upload-section.compact .file-label .icon {
    font-size: 1rem;
}

.upload-section.compact .submit-btn {
    width: fit-content;
    aspect-ratio: 1 / 1;

    display: inline-flex;
    justify-content: center;
    align-items: center;

    border-radius: 50%;
    padding: 0.5rem ;
}

</style>