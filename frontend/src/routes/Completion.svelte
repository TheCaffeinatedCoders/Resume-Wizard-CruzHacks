<script>
    let response = "";
    const endpoint = "http://127.0.0.1:8000/get-ai-response";
    let userInput = "";
    async function getResponse() {
        try {
            const data = await fetch(
                endpoint + "?field_name=&data=" + encodeURIComponent(userInput)
            );
            // const data = await fetch ('http://127.0.0.1:8000/get-ai-response?field_name=education&data=I%20am%20a%20student%20at%20the%20University%20of%20Washington%20studying%20computer%20science%20and%20mathematics.');
            response = await data.json();
            console.log(response);
        } catch (error) {
            console.error(error);
        }
    }

    async function getDoc() {
        let UserArgs = {
            name: "John Doe",
            phone: "555-555-1212",
            email: "test@example.com",
            github: "github.com/test",
            linkedin: "linkedin.com/test",
        };

        try {
            let response = await fetch(`http://127.0.0.1:8000/generate-doc`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(UserArgs),
            });
            let jsonData = await response.json();
            console.log(jsonData);
        } catch (error) {
            console.error(error);
        }
    }
</script>

<h1>Here is a sample completion response</h1>
<label for="prompt">Prompt:</label>
<input
    bind:value={userInput}
    type="text"
    id="prompt"
    name="prompt"
    placeholder="Insert some text here"
/>
<button type="button" on:click={getResponse}>Click Me!</button>
<p>Response: {response}</p>

<button on:click={getDoc}>Generate Doc</button>
