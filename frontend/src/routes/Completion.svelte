<script>
    let response = "";

    async function getResponse() {
        try {
            const data = await fetch('http://127.0.0.1:8000/');
            response = await data.json();
            console.log(response);
        } catch (error) {
            console.error(error);
        }
    }
</script>

<h1>Here is a sample completion response</h1>
<label for="prompt">Prompt:</label>
<input
    type="text"
    id="prompt"
    name="prompt"
    placeholder="Insert some text here"
/>
<button type="button" on:click={getResponse}>Click Me!</button>
<p>Response: {response.message}</p>
