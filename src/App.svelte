<script>
  import CreateCountry from './lib/CreateCountry.svelte';
  import CreateMissions from './lib/CreateMissions.svelte';
  import CreateMissions2 from './lib/CreateMissions2.svelte';
  import FlagMaker from './lib/FlagMaker.svelte';
  import logo from './assets/logo500x500.png';
  import {Img, Secondary, Heading, Tabs, TabItem} from "flowbite-svelte";
</script>

<main>
  <Img src="{logo}" class="logo" alignment="mx-auto" size="max-w-xs"/>
  <Heading tag="h1" class="mb-4" customSize="text-3xl font-extrabold  md:text-5xl lg:text-6xl">EU4 <Secondary class="ml-2">Nation Creator</Secondary></Heading>
  <div >
   <Tabs>
    <TabItem title="Create Country">
      <CreateCountry />
    </TabItem>
    <TabItem title="Create Missions">
      <!-- <CreateMissions /> -->
      <CreateMissions2/>
    </TabItem>
    <TabItem title="Flag Maker">
      <FlagMaker />
    </TabItem> 
  </Tabs>
  </div>
</main>

<style>
  .logo {
    height: 1em;
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
