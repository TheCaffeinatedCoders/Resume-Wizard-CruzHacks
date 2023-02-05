<script>
import {push, pop, replace} from 'svelte-spa-router'
</script>	
<p>
    <a href="#/test">Test route</a>
</p>
<h1>Resume Wizard</h1>
<h2>Whips up a resume via magic with ease</h2>
<!-- <button>Get Started</button> -->
<!-- <button onclick = "window.location.href = 'http://localhost:5000';">Get Started</button> -->
<button on:click={() => push('/info')}>Get Started</button>
<img src="/images/stars.png" alt="" width="203" height="105">
<style>
	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}
</style>
