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
                additonalEducationInfo: "",
            },
        ],
        workExperience: [
            {
                company: "",
                position: "",
                workStart: "",
                workEnd: "",
                additonalWorkInfo: "",
            },
        ],
        projects: [
            {
                name: "",
                description: "",
                stack: "",
                projectStart: "",
                projectEnd: "",
            },
        ],
        skills: [""],
    };

    $: currentSectionData = userData[currentSection];
    let currentAISuggestion = "";
    async function getAISuggauestion() {
        // console.log(currentSectionData);
        try {
            const aiResponse = await fetch(
                `http://127.0.0.1:8000/get-ai-response?field_name=${currentSection}&data=${encodeURIComponent(
                    // JSON.stringify(Object.values(currentSectionData))
                    JSON.stringify(currentSectionData.additonalEducationInfo)
                )}`
            );
            const jsonresponse = await aiResponse.json();
            currentAISuggestion = jsonresponse;
        } catch (error) {
            console.error(error);
        }
    }

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
    <div>
        <label for="additonalEducationInfo">Additional Education Info:</label>
        <input
            id="additonalEducationInfo"
            bind:value={currentSectionData.additonalEducationInfo}
        />
    </div>
    <button on:click={getAISuggauestion}>AI touch up</button>
    {#if currentAISuggestion}
        <p>{currentAISuggestion}</p>
    {/if}
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
        <label for="workStart">Start:</label>
        <input id="workStart" bind:value={currentSectionData.workStart} />
    </div>
    <div>
        <label for="workEnd">End:</label>
        <input id="workEnd" bind:value={currentSectionData.workEnd} />
    </div>
    <div>
        <label for="additonalWorkInfo">Additional Work Info:</label>
        <input
            id="additonalWorkInfo"
            bind:value={currentSectionData.additonalWorkInfo}
        />
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
        <label for="projectStart">Start:</label>
        <input id="projectStart" bind:value={currentSectionData.projectStart} />
    </div>
    <div>
        <label for="projectEnd">End:</label>
        <input id="projectEnd" bind:value={currentSectionData.projectEnd} />
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
