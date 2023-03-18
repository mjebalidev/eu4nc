<script>
  import CreateCountry from './lib/CreateCountry.svelte';
  import CreateMissions from './lib/CreateMissions.svelte';
  import FlagMaker from './lib/FlagMaker.svelte';
  import {Hr} from "flowbite-svelte";
</script>

<main>
  <div class="main-frame">
  <FlagMaker />
  <br/>
  <Hr/>
  <br/>
  <CreateCountry />
  <br/>
  <Hr />
  <br/>
  <CreateMissions />
  
  </div>
</main>

<style>
  .logo {
    height: 6em;
    padding: 1.5em;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 2em #646cffaa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 2em #ff3e00aa);
  }
  .read-the-docs {
    color: #888;
  }
  .main-frame {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
  }

</style>
