<script>
import { push } from "svelte-spa-router";
    let sections = [
        "personal_info",
        "objective",
        "education",
        "employment",
        "projects",
        "skills",
    ];
    let currentSection = "personal_info";
    let userData = {
        personal_info: [
            {
                name: "Carson Webster",
                email: "ccwebste@ucsc.edu",
                phone: "6193028234",
                github: "carsonwebster",
                linkedin: "carsonwebster"
            },
        ],
        objective: [
            {
                objective: ""
            },
        ],
        education: [
            {
                school_name: "",
                degree: "",
                gpa: "",
                school_description: "",
                school_start_date: "",
                school_end_date: ""
            },
        ],
        employment: [
            {
                company_name: "",
                company_city: "",
                job_name: "",
                job_start_date: "",
                job_end_date: "",
                job_description: "",
            },
        ],
        projects: [
            {
                project_name: "",
                project_start_date: "",
                project_end_date: "",
                project_description: "",
            },
        ],
        skills: [
            {
                skill_name: "",
                skill_description: "",
            },
        ],
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
    // const PDFDocument = require('pdfkit');
    // const fs = require('fs');
    async function getPDF() {
        try {
            const response = await fetch(`http://127.0.0.1:8000/generate-doc`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify(userData),
            });

            if (response.ok) {
                console.log("success");
                const latex = await response.json();
                console.log(latex);
                const blob = new Blob([latex], { type: "text/plain" });
                const link = document.createElement("a");
                link.download = "document.tex";
                link.href = URL.createObjectURL(blob);
                link.click();
            } else {
                console.error(await response.text());
            }
        } catch (error) {
            console.error(error);
        }
    }


</script>


<nav>
  <button class="homebutton" on:click={() => push("/")}>
    <img
      src="/images/LOGO.png"
      alt="logo"
      align="left"
      width="203"
      height="105"
    />
  </button>
</nav>
<div>
  <h1 class="title">Resume Wizard</h1>
  <h2 class="briefIntro">
    We are going to need some basic info from you to begin formatting your
    resume
  </h2>
</div>

<div id="container">
{#if currentSection === "personal_info"}
<h3>Personal Info</h3>
    <div>
        <label for="name">Name:</label>
        <input id="name" bind:value={currentSectionData[0].name} />
    </div>
    <div>
        <label for="email">Email:</label>
        <input id="email" bind:value={currentSectionData[0].email} />
    </div>
    <div>
        <label for="phone">Phone:</label>
        <input id="phone" bind:value={currentSectionData[0].phone} />
    </div>
    <div>
        <label for="github">Github:</label>
        <input id="github" bind:value={currentSectionData[0].github} />
    </div>
    <div>
        <label for="linkedin">Linkedin:</label>
        <input id="linkedin" bind:value={currentSectionData[0].linkedin} />
    </div>
{:else if currentSection === "objective"}
    <div>
        <label for="objective">Objective:</label>
        <input id="objective" bind:value={currentSectionData[0].objective} />
    </div>
  {:else if currentSection === "education"}
    <h3>Education</h3>

    <div>

        <label for="schoolName">School Name:</label>
        <input id="schoolName" bind:value={currentSectionData[0].schoolName} />
    </div>
    <div>
        <label for="degree">Degree:</label>
        <input id="degree" bind:value={currentSectionData[0].degree} />
    </div>
    <div>
        <label for="gpa">GPA:</label>
        <input id="gpa" bind:value={currentSectionData[0].gpa} />
    </div>
    <div>
        <label for ="school_description">School Description:</label>
        <input id="school_description" bind:value={currentSectionData[0].school_description} />
    </div>
    <div>
        <label for="school_start_date">School Start Date:</label>
        <input id="school_start_date" bind:value={currentSectionData[0].school_start_date} />
    </div>
    <div>
        <label for="school_end_date">School End Date:</label>
        <input id="school_end_date" bind:value={currentSectionData[0].school_end_date} />
    </div>
    <button class="button AIbutton" on:click={getAISuggauestion}
      >AI touch up</button
    >
    {#if currentAISuggestion}
      <p>{currentAISuggestion}</p>
    {/if}

{:else if currentSection === "employment"}
<h3>Work Experience</h3>
    <div>
        <label for="companyName">Company Name:</label>
        <input id="companyName" bind:value={currentSectionData[0].companyName} />
    </div>
    <div>
        <label for="company_city">Company City:</label>
        <input id="company_city" bind:value={currentSectionData[0].company_city} />
    </div>
    <div>
        <label for="job_name">Job Name:</label>
        <input id="job_name" bind:value={currentSectionData[0].job_name} />
    </div>
    <div>
        <label for="job_start_date">Job Start Date:</label>
        <input id="job_start_date" bind:value={currentSectionData[0].job_start_date} />
    </div>
    <div>
        <label for="job_end_date">Job End Date:</label>
        <input id="job_end_date" bind:value={currentSectionData[0].job_end_date} />
    </div>
    <div>
        <label for="job_description">Job Description:</label>
        <input id="job_description" bind:value={currentSectionData[0].job_description} />
    </div>
    <button class="button AIbutton" on:click={getAISuggauestion}
    >AI touch up</button
  >
  {#if currentAISuggestion}
    <p>{currentAISuggestion}</p>
  {/if}
  
  {:else if currentSection === "projects"}
    <h3>Projects</h3>
    <div>

        <label for="project_name">Project Name:</label>
        <input id="project_name" bind:value={currentSectionData[0].project_name} />
    </div>
    <div>
        <label for="project_start_date">Project Start Date:</label>
        <input id="project_start_date" bind:value={currentSectionData[0].project_start_date} />
    </div>
    <div>
        <label for="project_end_date">Project End Date:</label>
        <input id="project_end_date" bind:value={currentSectionData[0].project_end_date} />
    </div>
    <div>
        <label for="project_description">Project Description:</label>
        <input id="project_description" bind:value={currentSectionData[0].project_description} />
    </div>
    <button class="button AIbutton" on:click={getAISuggauestion}
    >AI touch up</button
  >
  {#if currentAISuggestion}
    <p>{currentAISuggestion}</p>
  {/if}
  {:else if currentSection === "skills"}
    <h3>Skills</h3>
    <div>
        <label for="skill_name">Skill Name:</label>
        <input id="skill_name" bind:value={currentSectionData[0].skill_name} />
    </div>
    <div>
        <label for="skill_description">Skill Description:</label>
        <input id="skill_description" bind:value={currentSectionData[0].skill_description} />

    </div>
  {/if}

  <div>
    <button
      class="button NextPrev"
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
                getPDF();
            }
            currentSection = sections[sections.indexOf(currentSection) + 1];
        }}
      class="button NextPrev">
      Next
    </button>
  </div>
</div>

<style>
  @import url("https://fonts.googleapis.com/css2?family=Itim&display=swap");
  @import url("https://fonts.googleapis.com/css2?family=Noto+Serif:ital,wght@0,400;0,700;1,400&display=swap");



  #container {
    margin: 0 auto;
    background-color: rgb(243, 222, 185);
    padding: 30px;
    border-radius: 50px;
    width: 60%;
    box-shadow: rgba(0, 0, 0, 0.4) 0px 2px 4px, rgba(0, 0, 0, 0.3) 0px 7px 13px -3px, rgba(0, 0, 0, 0.2) 0px -3px 0px inset;
  }

  input {
    background-color: #ffffff;
    display: inline;
  }

  .homebutton {
    width: 203px;
    height: 105px;
    padding: 0;
    background-color: #ffffff;
    color: #ffffff;
    border-style: hidden;
  }

  .formm {
    font-family: "Noto Serif", serif;
  }

  .title {
    font-family: "Itim", cursive;
    margin-top: 20px;
    margin-bottom: 20px;
  }

  .briefIntro {
    margin-bottom: 50px;
    font-family: "Itim", cursive;
    font-size: 20px;
    font-weight: 100;
  }

  .button {
    background-color: #ffffff; /*white*/
    border: none;
    color: white;
    padding: 16px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    margin: 4px 2px;
    transition-duration: 0.4s;
    cursor: pointer;
  }
  .AIbutton {
    background-color: rgba(238, 151, 224, 0.5);
    color: black;
    border: 2px solid rgba(238, 151, 224, 0.5);
    border-radius: 20px;
    width: 41%;
    /* margin-bottom: 50px; */
  }
  .AIbutton:hover {
    background-color: #ffffff;
    color: rgba(175, 174, 224, 10);
  }

  .NextPrev {
    background-color: rgba(175, 174, 224, 0.5);
    color: black;
    border: 2px solid rgba(175, 174, 224, 0.5);
    border-radius: 20px;
    width: 20%;
  }
  .NextPrev:hover {
    background-color: #ffffff;
    color: rgba(175, 174, 224, 10);
  }
</style>
