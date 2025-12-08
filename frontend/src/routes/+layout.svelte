<script lang="ts">
	import favicon from '$lib/assets/favicon.svg';
	import '$lib/styles/global.css';
	import '@fortawesome/fontawesome-free/css/all.min.css';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="background"></div>

<div class="layout-container">
	<header>
		<span>
			<i class="fa-solid fa-at">3cho</i>
		</span>
	</header>

	<main>
		{@render children()}
	</main>
	<footer>Desenvolvido por @gabriellsar</footer>
</div>

<style>

:global(body) {
	background: var(--color-background-dark);
    color : var(--color-text-dark);
    font-family: var(--font-family-body);
    margin: 20px;
}

.layout-container {
	display: flex;
	flex-direction: column;
	min-height: calc(100vh - 40px); 
}

main {
	flex: 1;
	display: flex;
	flex-direction: column;
}

.background {
	position: fixed;
	top: 100%;

	height: 100%;
	width: 100%;

	box-shadow: 0 0 200px 50px var(--color-accent-dark);

	z-index: -1;
}

footer {
	text-align: center;
	padding: 1rem 0;
	font-size: 0.7rem;
	color: var(--color-text-dark);
	margin-top: auto;
}

</style>
