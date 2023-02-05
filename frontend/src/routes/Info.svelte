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


<style>
    @import url('https://fonts.googleapis.com/css2?family=Itim&display=swap');

    div {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;

        display: flex;
        align-items: center;
        justify-content: center;
        flex-flow: column;
        background-color: rgba(175, 174, 224, 0.39);
    }

    h1 {
        font-family: 'Itim', cursive;
        margin-top: 20px;
        margin-bottom: 20px;
    }

    h2 {
        margin-bottom: 50px;
        font-family: 'Itim', cursive;
        font-size: 20px;
        font-weight: 100;
    }

    .button{
		background-color: #ffffff;/*white*/
		border: none;
		color:white;
		padding: 16px 32px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 16px;
		margin: 4px 2px; 
		transition-duration:0.4s;
		cursor:pointer; 
	}
	.button1{
		background-color: rgba(175, 174, 224, 0.5);
		color:black;
		border: 2px solid #ffffff;; 
		border-radius:20px;
		width: 70%;
		/* margin-bottom: 50px; */
	}
	.button1:hover{
		background-color: #ffffff;
		color: rgba(175, 174, 224, 10); 
	}
    .button2{
		background-color: rgba(175, 174, 224, 0.5);
		color:black;
		border: 2px solid #ffffff;; 
		border-radius:20px;
		width: 80%;
		/* margin-bottom: 50px; */
	}
	.button2:hover{
		background-color: #ffffff;
		color: rgba(175, 174, 224, 10); 
	}

</style>
