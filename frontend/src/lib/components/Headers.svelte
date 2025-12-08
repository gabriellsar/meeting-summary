<script lang="ts">
    import {slide} from 'svelte/transition';
    import {quintOut} from 'svelte/easing';

    let { parsedSummary } = $props();
    let crr: boolean = $state(false);
    let headings: { id: string; text: string; level: number }[] = $state([]);

    function onclick() {
        crr = !crr;
    }    

    function extractHeadings(htmlString: string) {
        if (!htmlString) return [];
        
        const parser = new DOMParser();
        const doc = parser.parseFromString(htmlString, 'text/html');
        
        const elements = Array.from(doc.querySelectorAll('h1, h2, h3'));

        return elements.map((el) => {
            return {
                text: el.textContent || '',
                level: Number(el.tagName.substring(1)),
                id: el.id
            };
        });
    }

    $effect(() => {
        headings = extractHeadings(parsedSummary);
    });

    function scrollToHeading(id: string) {
        const element = document.getElementById(id);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth', block: 'start' });
        } else {
            console.warn('Elemento não encontrado. Certifique-se que o HTML renderizado possui os mesmos IDs.');
        }
    }

</script>


<div class="guide-container" class:open={crr}>
    
    <button 
        class="header-trigger" 
        {onclick}
        title="Mostrar/Ocultar Guias"
        aria-expanded={crr}
    >
        <div class="icon-area">
            <i class="fa-solid fa-grip-lines" class:rotated={crr}></i>
        </div>
    
        <span class="label">
            Guias
        </span>
    </button>

    {#if crr}
        <div 
            class="content-wrapper"
            transition:slide={{ axis: 'y', duration: 500, easing: quintOut }}
        >   
            <div class="separator"></div>

            <ul class="guide-list">
                {#each headings as heading}
                    <li>
                        <button 
                            class="guide-item level-{heading.level}" 
                            onclick={() => scrollToHeading(heading.id)}
                        >
                            {heading.text}
                        </button>
                    </li>
                {:else}
                    <li class="empty-state">Nenhum título encontrado</li>
                {/each}
            </ul>
        </div>
    {/if}
</div>

<style>
    .guide-container {
        display: flex;
        flex-direction: column;
        width: 40px; 
        border-radius: 20px;
        background-color: var(--color-background-dark);
        border: 1px solid transparent;
        overflow: hidden;
        transition: 
            width 0.5s cubic-bezier(0.25, 0.8, 0.25, 1),
            background-color 0.3s ease,
            box-shadow 0.3s ease,
            border-radius 0.3s ease,
            border-color 0.3s ease;
    }

    .guide-container:not(.open):hover {
        width: 120px;
        background-color: var(--color-background-dark);
        border-color: var(--color-secondary-dark);
    }

    .guide-container.open {
        width: 300px;
        background-color: var(--color-background-dark);
        border-radius: 16px;
        border-color: var(--color-secondary-dark);
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.5);
    }

    .header-trigger {
        display: flex;
        align-items: center;
        width: 100%;
        height: 40px;
        min-height: 40px;
        border: none;
        background: transparent;
        cursor: pointer;
        padding: 0;
        outline: none;
    }

    .icon-area {
        width: 40px; 
        height: 40px;
        min-width: 40px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .header-trigger i {
        font-size: 1.2rem;
        color: var(--color-text-dark);
        transition: transform 0.5s ease;
    }

    .rotated {
        transform: rotate(90deg);
    }

    .label {
        white-space: nowrap; 
        padding-right: 15px;
        font-family: var(--font-family-headings);
        font-weight: 500;
        color: var(--color-text-dark);
        opacity: 0;
        transform: translateX(-10px);
        transition: opacity 0.3s ease, transform 0.3s ease;
    }

    .guide-container:hover .label,
    .guide-container.open .label {
        opacity: 1;
        transform: translateX(0);
        transition-delay: 0.1s;
    }

    .content-wrapper {
        display: flex;
        flex-direction: column;
        width: 100%;
        max-height: 400px;
        overflow-y: auto;
    }

    .content-wrapper::-webkit-scrollbar {
        width: 6px;
    }

    .content-wrapper::-webkit-scrollbar-track {
        background: transparent;
    }

    .content-wrapper::-webkit-scrollbar-thumb {
        background-color: var(--color-secondary-dark);
        border-radius: 3px;
    }

    .separator {
        height: 1px;
        background-color: var(--color-secondary-dark);
        margin: 0 16px 8px 16px;
        opacity: 0.3;
    }

    .guide-list {
        list-style: none;
        padding: 0;
        margin: 0 0 12px 0;
    }

    .guide-item {
        display: block;
        width: 100%;
        text-align: left;
        background: none;
        border: none;
        padding: 8px 16px;
        cursor: pointer;
        color: var(--color-text-dark);
        font-family: var(--font-family-body);
        font-size: 0.9rem;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
        border-left: 3px solid transparent;
        transition: all 0.2s ease;
        opacity: 0.8;
    }

    .guide-item:hover {
        background-color: var(--color-secondary-dark);
        color: var(--color-primary-dark);
        border-left: 3px solid var(--color-accent-dark);
        opacity: 1;
    }

    .level-1 { 
        padding-left: 16px; 
        font-weight: 700;
        color: var(--color-primary-dark);
    }
    
    .guide-item.level-1:hover {
        color: var(--color-text-dark);
    }

    .level-2 { 
        padding-left: 32px; 
        font-size: 0.85rem; 
    }

    .level-3 { 
        padding-left: 48px; 
        font-size: 0.8rem; 
        opacity: 0.6; 
    }

    .empty-state {
        padding: 20px;
        text-align: center;
        color: var(--color-secondary-light);
        font-family: var(--font-family-body);
        font-size: 0.9rem;
    }
</style>