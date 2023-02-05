<script>
    let count = 0;
    let dictionary = {
    name: "",
    age: "",
    phone: "",
  };
//   Create a funciton to append a new key and empty value into the dictionary
    function addKey() {
        dictionary[count] = "";
        count++;
        dictionary = {...dictionary};
    }
    function updateValue(key, event) {
    dictionary[key] = event.target.value;
  }

  // Function to print all the data at the bottom of the screen on button press
    function printData() {
        let data = "";
        for (let key in dictionary) {
        data += key + ": " + dictionary[key] + "\n";
        }
        alert(data);
    }
</script>

<h1>Resume Wizard</h1>
<h2>We are going to need some basic info from you to begin formatting your resume</h2>
<form>
{#each Object.entries(dictionary) as [key, value]}
  <div>
    <label for={key}>{key}:</label>
    <input id={key} bind:value={value} on:input={(event) => updateValue(key, event)} />
  </div>
{/each}
</form>

<button on:click={addKey}>Add Key</button>
<button on:click={printData}>Print Data</button>


<!-- <form>
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

    <h3>Education</h3>
    <label for="school">School</label>
    <input type="text" id="school" name="school" placeholder="Your school..">
    <label for="degree">Degree</label>
    <input type="text" id="degree" name="degree" placeholder="Your degree..">
    <label for="graduation">Graduation</label>
    <input type="text" id="graduation" name="graduation" placeholder="Your graduation..">
    <label for = "moreeducation">Add More</label>
    <button type = "button" onclick = "alert('Added Education Slot');">Add Education</button> 

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

    <h3>Skills</h3>
    <label for="skill1">Skill 1</label>
    <input type="text" id="skill1" name="skill1" placeholder="Your skill..">
    <label for="skill2">Skill 2</label>
    <input type="text" id="skill2" name="skill2" placeholder="Your skill..">
    <label for="skill3">Skill 3</label>
    <input type="text" id="skill3" name="skill3" placeholder="Your skill..">
    <label for = "skilli">Add More</label>
    <button type = "button" onclick = "alert('Added Skill Slot');">Add Skills</button> 
    <!-- <input type ="button" id = "skilli" name="skilli"> -->
