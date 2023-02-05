<script>
    let sections = [
        "personalInfo",
        "education",
        "workExperience",
        "projects",
        "skills",
    ];
    let currentSection = "personalInfo";
    let userData = {
        personalInfo: [
            {
                name: "",
                email: "",
                phone: "",
                objective: "",
            },
        ],
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

    $: currentSectionData = userData[currentSection];

    // function nextSection() {
    //     if (currentSection === "personalInfo") {
    //             return;
    //         }
    //         currentSection = sections[sections.indexOf(currentSection) - 1]; 
    // }
    // function previousSection() {
    //     if (currentSection === "skills") {
    //             alert(userData);
    //         }
    //         currentSection = sections[sections.indexOf(currentSection) + 1]; 
    // }
</script>

<h1>Resume Wizard</h1>
<h2>
    We are going to need some basic info from you to begin formatting your
    resume
</h2>

<h3>{currentSection}</h3>
{#if currentSection === "personalInfo"}
    <div>
        <label for="name">Name:</label>
        <input id="name" bind:value={currentSectionData.name} />
    </div>
    <div>
        <label for="email">Email:</label>
        <input id="email" bind:value={currentSectionData.email} />
    </div>
    <div>
        <label for="phone">Phone:</label>
        <input id="phone" bind:value={currentSectionData.phone} />
    </div>
    <div>
        <label for="objective">Objective:</label>
        <input id="objective" bind:value={currentSectionData.objective} />
    </div>
{:else if currentSection === "education"}
    <div>
        <label for="school">School:</label>
        <input id="school" bind:value={currentSectionData.school} />
    </div>
    <div>
        <label for="degree">Degree:</label>
        <input id="degree" bind:value={currentSectionData.degree} />
    </div>
    <div>
        <label for="graduation">Graduation:</label>
        <input id="graduation" bind:value={currentSectionData.graduation} />
    </div>
{:else if currentSection === "workExperience"}
    <div>
        <label for="company">Company:</label>
        <input id="company" bind:value={currentSectionData.company} />
    </div>
    <div>
        <label for="position">Position:</label>
        <input id="position" bind:value={currentSectionData.position} />
    </div>
    <div>
        <label for="start">Start:</label>
        <input id="start" bind:value={currentSectionData.start} />
    </div>
    <div>
        <label for="end">End:</label>
        <input id="end" bind:value={currentSectionData.end} />
    </div>
{:else if currentSection === "projects"}
    <div>
        <label for="name">Name:</label>
        <input id="name" bind:value={currentSectionData.name} />
    </div>
    <div>
        <label for="description">Description:</label>
        <input id="description" bind:value={currentSectionData.description} />
    </div>
    <div>
        <label for="stack">Stack:</label>
        <input id="stack" bind:value={currentSectionData.stack} />
    </div>
    <div>
        <label for="start">Start:</label>
        <input id="start" bind:value={currentSectionData.start} />
    </div>
    <div>
        <label for="end">End:</label>
        <input id="end" bind:value={currentSectionData.end} />
    </div>
{:else if currentSection === "skills"}
    <div>
        <label for="skill">Skill:</label>
        <input id="skill" bind:value={currentSectionData[0]} />
    </div>
{/if}
<div>
    <button
        type="button"
        on:click={() => {
            if (currentSection === "personalInfo") {
                return;
            }
            currentSection = sections[sections.indexOf(currentSection) - 1];
        }}
    >
        Previous
    </button>
    <button
        type="button"
        on:click={() => {
            if (currentSection === "skills") {
                alert(JSON.stringify(userData));
            }
            currentSection = sections[sections.indexOf(currentSection) + 1];
        }}
    >
        Next
    </button>
</div>
