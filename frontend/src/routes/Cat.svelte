<script>
    import { onMount } from 'svelte';
  
    let data;
  
    onMount(async () => {
      try {
        const response = await fetch('https://catfact.ninja/fact');
        data = await response.json();
      } catch (error) {
        console.error(error);
      }
    });
</script>

<h1>CAT FACT</h1>
{#await data}
  <p>Loading...</p>
{:then}
  {#if data}
    <p>{data.fact}</p>
  {:else}
    <p>Sorry, an error occurred while fetching the data.</p>
  {/if}
{/await}
  