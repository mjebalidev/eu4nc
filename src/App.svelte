<script>
  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  import CreateCountry from './lib/CreateCountry.svelte';
  import CreateEvents from './lib/CreateEvents.svelte';
  import FlagMaker from './lib/FlagMaker.svelte';
  import CreateMissions from './lib/CreateMissions.svelte';
</script>

<main>
  <CreateMissions />

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
</style>
