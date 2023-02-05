<script>
import {push, pop, replace} from 'svelte-spa-router'
</script>	

<h10> </h10>  
<div class="head_section"><img src="/images/LOGO.png" alt="logo" align = "left" width="203" height="105"></div>

<div class="main_section">	
<p class="homepage_logo"><img src="/images/HOMEPAGE ART.png" alt="homepage art"width="654" height="267"></p>  

<h1 style="font-size:60px;">Resume Wizard</h1>
<!-- <h2>Whips up a resume via magic with ease</h2> -->
<!-- <button>Get Started</button> -->
<!-- <button onclick = "window.location.href = 'http://localhost:5000';">Get Started</button> -->
<button class="button button1" on:click={() => push('/info')}>Start</button>
<!-- <button type = "button" on:click={() => push('/info')}>Start</button>  -->
</div>
<style>
	@import url('https://fonts.googleapis.com/css2?family=Itim&display=swap');
	div {
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
		bottom: 0;

        background-color: rgba(175, 174, 224, 0.5);
    }

	h1 {
		font-family: 'Itim', cursive;
        margin-top: 40px;
        margin-bottom: 40px;

	}
	.homepage_logo{
		padding-top: 100px;
		padding-left: 100px;
		margin-top: 100px;

	}
	.main_section{
		display: flex;
        align-items: center;
        justify-content: center;
        flex-flow: column;
	}
	.head_section{
		background-color: rgba(175, 174, 224, 0.0);
		margin-left: 16px;
		margin-top: 16px;
		
	}
	.button{
		background-color: #ffffff;/*white*/
		border: none;
		color:white;
		padding: 16px 32px;
		text-align: center;
		text-decoration: none;
		display: inline-block;
		font-size: 30px;
		margin: 4px 2px; 
		transition-duration:0.4s;
		cursor:pointer; 
	}
	.button1{
		background-color: rgba(175, 174, 224, 0.5);
		color:black;
		border: 2px solid #ffffff;; 
		border-radius:20px;
		width: 25%;
		margin-bottom: 50px;
	}
	.button1:hover{
		background-color: #ffffff;
		color: rgba(175, 174, 224, 10); 
	}
</style>
