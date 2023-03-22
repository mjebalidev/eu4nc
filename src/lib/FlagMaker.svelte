<script>
    import {Hr, Button} from 'flowbite-svelte'
</script>
  
<main>
    <Button color="dark" href="https://flagmakerjr.stg7.net/" target="_blank">Go to flagmakerjr.stg7.net</Button>
    <Hr />
    <div class="container">
        <iframe id="flagmaker"
        title="flagmaker"
        width="500"
        height="500"
        class="responsive-iframe"
        src="https://flagmakerjr.stg7.net/"></iframe>
    </div>
</main>
  
<style>

.container {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    height: 100%;
    width: 100%;
}

</style>