<script lang="ts">
    import { marked } from 'marked';
    import Headers from './Headers.svelte';
    import Documentation from './Documentation.svelte';

    function slugify(text: string) {
        return text
            .toString()
            .toLowerCase()
            .trim()
            .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
            .replace(/\s+/g, '-')
            .replace(/[^\w\-]+/g, '')
            .replace(/\-\-+/g, '-');
    }

    const renderer = {
        heading({ text, depth }: { text: string; depth: number }) {
            const id = slugify(text);
            return `<h${depth} id="${id}">${text}</h${depth}>`;
        }
    };

    marked.use({ renderer });

    let { summary = "" } = $props();
    let parsedSummary = $derived(marked.parse(summary));
    
</script>

<main>
    <Headers {parsedSummary} />
    <Documentation {parsedSummary} />
</main>

<style>

</style>