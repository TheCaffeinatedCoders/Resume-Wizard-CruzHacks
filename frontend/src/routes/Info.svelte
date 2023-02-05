<script>
    // let count = 0;
    // let dictionary = {
    //     name: "",
    //     age: "",
    //     phone: "",
    // };
    let sections = [
        "personalInfo",
        "education",
        "workExperience",
        "projects",
        "skills",
    ];
    let currentSection = "personalInfo";
    let userData = {
        personalInfo: {
            firstName: "Carson",
            lastName: "",
            email: "",
            phone: "",
            objective: "",
        },
        education: [
            {
                school: "",
                degree: "",
                graduation: "",
            },
        ],
        workExperience: [
            {
                company: "",
                position: "",
                start: "",
                end: "",
            },
        ],
        projects: [
            {
                name: "",
                description: "",
                stack: "",
                start: "",
                end: "",
            },
        ],
        skills: [""],
    };
    //   Create a funciton to append a new key and empty value into the dictionary
    // function addKey() {
    //     dictionary[count] = "";
    //     count++;
    //     dictionary = { ...dictionary };
    // }
    // function updateValue(key, event) {
    //     dictionary[key] = event.target.value;
    // }

    // Function to print all the data at the bottom of the screen on button press
    // function printData() {
    //     let data = "";
    //     for (let key in dictionary) {
    //         data += key + ": " + dictionary[key] + "\n";
    //     }
    //     alert(data);
    // }
</script>

<h1>Resume Wizard</h1>
<h2>
    We are going to need some basic info from you to begin formatting your
    resume
</h2>
<form>
    {#each Object.entries(userData) as [key, value]}
        {#if key == currentSection}
            <h3>{currentSection}</h3>
            <!-- <p>{value.jsonStringify()}</p> -->
            <p>{JSON.stringify(value)}</p>
            {#each Object.entries(value) as [prompt, input]}
                <div>
                    <label for={prompt}>{prompt}:</label>
                    <input
                        id={prompt}
                        bind:value={userData.currentSection.input}
                    />
                </div>
            {/each}
        {/if}
        <button
            on:click={() =>
                (currentSection =
                    sections[sections.indexOf(currentSection) + 1])}>Next</button>
    {/each}
</form>
<!-- <form>
    {#each Object.entries(userData) as [key, value]}
        <div>
            <label for={key}>{key}:</label>
            <input
                id={key}
                bind:value
                on:input={(event) => updateValue(key, event)}
            />
        </div>
    {/each}
</form> -->
