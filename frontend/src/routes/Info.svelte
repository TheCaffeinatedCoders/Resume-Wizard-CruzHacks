<script>

let emptyForm = { company: '', position: '', start: '', end: '' };
  let Objects = [emptyForm];

  function addObject() {
    Objects.push(emptyForm);
    Objects = [...Objects];
  }
</script>


<div>
    <h1>Resume Wizard</h1>
    <h2>We are going to need some basic info from you to begin formatting your resume</h2>

    <!-- <img src="../images/witch-broom.png" alt="broom"> -->

    <form>
        <h3>Personal Information</h3>
        <label for="name">Name</label>
        <input type="text" id="name" name="name" placeholder="Your name..">
        <label for="email">Email</label>
        <input type="text" id="email" name="email" placeholder="Your email..">
        <label for="phone">Phone</label>
        <input type="text" id="phone" name="phone" placeholder="Your phone number..">
        <label for="address">Address</label>
        <input type="text" id="address" name="address" placeholder="Your address..">
        <label for="city">City</label>
        <input type="text" id="city" name="city" placeholder="Your city..">
        <label for="state">State</label>
        <input type="text" id="state" name="state" placeholder="Your state..">
    </form>
    
    <form>
        <h3>Education</h3>
        <label for="school">School</label>
        <input type="text" id="school" name="school" placeholder="Your school..">
        <label for="degree">Degree</label>
        <input type="text" id="degree" name="degree" placeholder="Your degree..">
        <label for="graduation">Graduation</label>
        <input type="text" id="graduation" name="graduation" placeholder="Your graduation..">
        <label for = "moreeducation">Add More</label>
        <button type = "button" onclick = "alert('Added Education Slot');">Add Education</button> 
    </form>

    <!-- <form> My Code
        <h3>Work Experience</h3>
        <label for="company">Company</label>
        <input type="text" id="company" name="company" placeholder="Your company..">
        <label for="position">Position</label>
        <input type="text" id="position" name="position" placeholder="Your position..">
        <label for="start">Start</label>
        <input type="text" id="start" name="start" placeholder="Your start..">
        <label for="end">End</label>
        <input type="text" id="end" name="end" placeholder="Your end..">
        <label for = "morejobs">Add More</label>
        <button type = "button" onclick = "alert('Added Job Slot');">Add Jobs</button> 
    </form> -->

    <form>
        <h3>Work Experience</h3>
        {#each Objects as object}
          <label for="company">Company</label>
          <input type="text" id="company" bind:value={object.company} placeholder="Your company..">
          <label for="position">Position</label>
          <input type="text" id="position" bind:value={object.position} placeholder="Your position..">
          <label for="start">Start</label>
          <input type="text" id="start" bind:value={object.start} placeholder="Your start..">
          <label for="end">End</label>
          <input type="text" id="end" bind:value={object.end} placeholder="Your end..">
        {/each}
        <label for="morejobs">Add More</label>
        <button type="button" on:click={addObject}>
          Add Jobs
        </button>
    </form>


    <form>
        <h3>Skills</h3>
        <label for="skill1">Skill 1</label>
        <input type="text" id="skill1" name="skill1" placeholder="Your skill..">
        <label for="skill2">Skill 2</label>
        <input type="text" id="skill2" name="skill2" placeholder="Your skill..">
        <label for="skill3">Skill 3</label>
        <input type="text" id="skill3" name="skill3" placeholder="Your skill..">
        <label for = "skilli">Add More</label>
        <button type = "button" onclick = "alert('Added Skill Slot');">Add Skills</button> 

    </form>


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

</style>
