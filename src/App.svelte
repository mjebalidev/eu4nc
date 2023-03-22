<script>
  import CreateCountry from './lib/CreateCountry.svelte';
  import CreateMissions from './lib/CreateMissions.svelte';
  import CreateMissions2 from './lib/CreateMissions2.svelte';
  import CreateEvents from './lib/CreateEvents.svelte';
  import FlagMaker from './lib/FlagMaker.svelte';
  import logo from './assets/logo500x500.png';
  import {Img, Secondary, Heading, Tabs, TabItem} from "flowbite-svelte";
  import Footer from './lib/Footer.svelte';
  import { DarkMode } from 'flowbite-svelte';
</script>

<main class="main-frame">
  <div>
    <div class="darkmode">
      <DarkMode />
    </div>
    <div class="logo">
      <Img src="{logo}" alignment="mx-auto" size="max-w-xs"/>
    </div>
      <Heading tag="h1" class="mb-4" customSize="text-3xl font-extrabold  md:text-5xl lg:text-6xl">EU4 <Secondary class="ml-2">Nation Creator</Secondary></Heading>
    <div >
      <Tabs style="full" color="primary">
        <TabItem title="Create Country">
          <CreateCountry />
        </TabItem>
        <TabItem title="Create Missions">
          <!-- <CreateMissions /> -->
          <CreateMissions2/>
        </TabItem>
        <TabItem title="Create Events">
          <CreateEvents />
        </TabItem>
        <TabItem title="Flag Maker">
          <FlagMaker />
        </TabItem> 
      </Tabs>
    </div>
    <div class="footer" color="primary">
      <Footer />
    </div>
  </div>
</main>

<style>
  .logo {
    height: auto;
    will-change: filter;
    transition: filter 300ms;
  }
  .logo:hover {
    filter: drop-shadow(0 0 1em #551717aa);
  }
  .logo.svelte:hover {
    filter: drop-shadow(0 0 1em #a22a01aa);
  }
  .read-the-docs {
    color: #888;
  }
  .main-frame {
    align-items: center;
    height: 100%;
    width: 100%;
    margin-bottom: 5%;
  }
  .darkmode{
    position: fixed;
    right: 0;
    top: 0;
    width: 100%;
    text-align: right;
  }
  .footer{
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        color: black;
        text-align: center;
    }

</style>
