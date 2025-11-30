<script lang="ts">
    import { marked } from 'marked';

    let { summary = "" } = $props();

    let message: string = $state("");
    let textAreaRef: HTMLTextAreaElement | undefined = $state();
    
    let parsedSummary = $derived(marked.parse(summary));

    $effect(() => {
        message;

        if (textAreaRef) {
            textAreaRef.style.height = 'auto';
            textAreaRef.style.height = textAreaRef.scrollHeight + 'px';
        }
    })

</script>

<div class="summary-view">
    <div class="content-display">    
        <div class="markdown-body">
            {@html parsedSummary}
        </div>
    </div>

    <div class="input-container">
        <textarea 
            placeholder="Pesquisar..." 
            bind:value={message}
            bind:this={textAreaRef}
        ></textarea>
        <button type="submit" aria-label="Enviar" title="Enviar">
            <i class="fa-solid fa-circle-play" aria-hidden="true"></i>
        </button>
    </div>
</div>

<style>
    .summary-view {
        position: relative;
        width: calc(100% - 20px);
        height: 79vh;

        background-color: #1E1F20;

        margin-top: 10px;
        border-radius: 20px;
        padding: 10px;
        overflow: hidden;

        scrollbar-color: transparent transparent;
    }
    .content-display {
        position: absolute;
        top: 0px;
        left: 0px;
        right: 0px;
        bottom: 60px;

        overflow-y: auto;
        padding: 20px;
        box-sizing: border-box; 
    }
    .input-container {
        position: absolute;
        left: 0px;
        right: 0px;
        bottom: 0px;

        max-height: 200px; 
        display: flex;
        align-items: flex-end;
        align-items: center;
        
        background-color: #1E1F20;
        border-top: 5px solid var(--color-background-dark);

        overflow: hidden;
        padding: 10px;

        box-sizing: border-box; 
        color: var(--color-primary-dark);

        box-shadow: 0 -30px 15px var(--color-background-dark)
    }

    textarea {
        flex-grow: 1;
        background: transparent;
        font-size: 1rem;
        resize: none;
        border: none;
        outline: none;
        color: var(--color-text-dark);
    }

    button {
        border-radius: 50%;
        background: transparent;
        border: none;
        cursor: pointer;

        width: 40px;
        height: 40px;
        margin: 0 15px 0 0;
        
    }
    button i {
        font-size: 40px;
        color: var(--color-text-dark);
    }

    button:hover i {
        color: var(--color-primary-dark);
    }

</style>