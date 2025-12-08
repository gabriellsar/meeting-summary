<div class="container">
    <div class="loader"></div>
</div>

<style>
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 2rem 0;
    }

    .loader {
        width: 50px;
        aspect-ratio: 1;
        border-radius: 50%;
        border: 8px solid;
        border-color: var(--color-primary-dark) var(--color-background-dark);
        animation: l1 1s infinite;
    }
    @keyframes l1 {
        to{
            transform: rotate(.5turn)
        }
    }
</style>