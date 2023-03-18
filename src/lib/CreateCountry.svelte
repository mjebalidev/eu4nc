<script>
import { Label, Input, Button,Search, Checkbox} from 'flowbite-svelte'
import provinces_filelist from '../lib/provinces_list.txt'

let display_result = false

// tag
let tag = "ZAA" // 3 letters
let country_name = "Zaaland" // global
// global
let gouvernements = ["stateless_society","pirate_government","pirate_kingdom","holy_roman_electors_monarchy","holy_roman_electors_republic","japanese_shogunate","french_kingdom","default_monarchy","default_republic","default_theocracy","default_tribal","gov_steppe_horde","gov_native_council","noble_republic","gov_republican_dictatorship","gov_papal_government","gov_tribal","germanic_monastic_order","brewing_order","jewish_theocracy","zoroastrian_theocracy","orthodox_theocracy"]
let religions = ["ibadi","shiite","sunni","coptic","reformed","protestant","hussite","anglican","catholic","orthodox","paganism","jewish","zoroastrianism","buddhism","hinduism","islam","jainism","sikhism","shinto","taoism","confucianism","totemism","shamanism","animism"]
let graphical_cultures = []

// history - countries - ZAA
let gouvernement = ""
let add_government_reform = ""
let primary_culture = ""
let religion = ""
let elector = ""
let capital = ""
let technology_group = ""
let add_accepted_culture = ""
let change_estate_land_share = "{ estate = estate_burghers share = -5 }"
let monarch_name = ""
let monarch_dynastie = ""
let monarch_adm = ""
let monarch_dip = ""
let monarch_mil = ""
let monarch_birth_date = "1423.1.1"
let monarch_religion = ""
let monarch = `{ name = "${monarch_name}" dynasty = "${monarch_dynastie}" birth_date = ${monarch_birth_date} adm = ${monarch_adm} dip = ${monarch_dip} mil = ${monarch_mil} religion = ${monarch_religion} }`

// common - countries - ZAA
let graphical_culture = ""
let color = "{ 0 0 0 }"
let revolutionnary_colors = "{ 0 0 0 }"
let prefered_religion = ""
let historical_idea_groups = ""
let historical_units = ""
let monarch_names = ""
let leader_names = ""
let ship_names = ""


// provinces
let provinces = []
let searched_provinces = []
let provinces_toadd = []
// list all file provinces_list.txt in array provinces
let owned_provinces = ""
let value = ""

function listProvinces(province){
    console.log("input:"+province)
    // list all items and check if the search value is in the item
    searched_provinces = provinces.filter(item => item.includes(province))
    console.log(searched_provinces)
}

let lines = [];

async function loadFile() {
    const response = await fetch(provinces_filelist);
    const text = await response.text();
    lines = text.split('\n');
    provinces = lines
}

function addProvince(current){
    if(!provinces_toadd.includes(current)){
        provinces_toadd.push(current)
    }
    else{
        const index = provinces_toadd.indexOf(current);
        if (index > -1) {
            provinces_toadd.splice(index, 1);
        }
    }
    console.log(provinces_toadd)
}

function createCountry(){
    // create the file
    // end files
    // /country_tags/00_counteries.txt
    let countries_00_tag = `${tag} = "countries/${tag}custom.txt"`

    // history/countries/ZAA - ZAAcustom.txt
    let end_history_countries = `
    gouvernement = ${gouvernement}
    add_government_reform = ${add_government_reform}
    primary_culture = ${primary_culture}
    religion = ${religion}
    elector = ${elector}
    capital = ${capital}
    technology_group = ${technology_group}
    add_accepted_culture = ${add_accepted_culture}
    change_estate_land_share = ${change_estate_land_share}
    1444.1.1 = { 
        monarch = ${monarch}
    }
    `

    // common/countries/ZAA - ZAAcustom.txt
    let end_common_countries = `
    graphical_culture = ${graphical_culture}
    color = ${color}
    revolutionnary_colors = ${revolutionnary_colors}
    prefered_religion = ${prefered_religion}
    historical_idea_groups = ${historical_idea_groups}
    historical_units = ${historical_units}
    monarch_names = ${monarch_names}
    leader_names = ${leader_names}
    ship_names = ${ship_names}
    `
    // provinces
    // provinces_toadd

    downloadFile("00_countries",countries_00_tag)
    downloadFile(tag + " - " + country_name,end_history_countries)
    downloadFile(country_name,end_common_countries)
    display_result = true
}   

function downloadFile(name,file) {

    // Create a new file blob from the contents
    const fileBlob = new Blob([file], { type: 'text/plain' });

    // Create a URL for the file blob
    const fileUrl = URL.createObjectURL(fileBlob);

    // Create a new anchor element
    const link = document.createElement('a');

    // Set the download attribute and file URL
    link.download = name +'.txt';
    link.href = fileUrl;

    // Add the anchor element to the DOM
    document.body.appendChild(link);

    // Click the anchor element to initiate the download
    link.click();

    // Remove the anchor element from the DOM
    document.body.removeChild(link);

    // Revoke the URL to free up memory
    URL.revokeObjectURL(fileUrl);
  }

loadFile()
</script>
  
<main>
    <div>
        <Label>Tag</Label>
        <Input bind:value={tag} />
        <Label>Country Name</Label>
        <Input bind:value={country_name} />
        <Label>Government</Label>
        <Input bind:value={gouvernement} />
        <Label>Government reform</Label>
        <Input bind:value={add_government_reform} />
        <Label>Primary culture</Label>
        <Input bind:value={primary_culture} />
        <Label>Religion</Label>
        <Input bind:value={religion} />
        <Label>Elector</Label>
        <Input bind:value={elector} />
        <Label>Capital</Label>
        <Input bind:value={capital} />
        <Label>Technology group</Label>
        <Input bind:value={technology_group} />
        <Label>Accepted culture</Label>
        <Input bind:value={add_accepted_culture} />
        <Label>Change estate land share</Label>
        <Input bind:value={change_estate_land_share} />
        <Label>Monarch name</Label>
        <Input bind:value={monarch_name} />
        <Label>Monarch dynastie</Label>
        <Input bind:value={monarch_dynastie} />
        <Label>Monarch adm</Label>
        <Input bind:value={monarch_adm} />
        <Label>Monarch dip</Label>
        <Input bind:value={monarch_dip} />
        <Label>Monarch mil</Label>
        <Input bind:value={monarch_mil} />
        <Label>Monarch birth date</Label>
        <Input bind:value={monarch_birth_date} />
        <Label>Monarch religion</Label>
        <Input bind:value={monarch_religion} />
        <Label>Graphical culture</Label>
        <Input bind:value={graphical_culture} />
        <Label>Color</Label>
        <Input bind:value={color} />
        <Label>Revolutionnary colors</Label>
        <Input bind:value={revolutionnary_colors} />
        <Label>Prefered religion</Label>
        <Input bind:value={prefered_religion} />
        <Label>Historical idea groups</Label>
        <Input bind:value={historical_idea_groups} />
        <Label>Historical units</Label>
        <Input bind:value={historical_units} />
        <Label>Monarch names</Label>
        <Input bind:value={monarch_names} />
        <Label>Leader names</Label>
        <Input bind:value={leader_names} />
        <Label>Ship names</Label>
        <Input bind:value={ship_names} />


        <h2>Add your provinces</h2>
        <Search bind:value on:input={()=> listProvinces(value)}>
        </Search>
        {#each searched_provinces as found_province}
            <p>{found_province}</p>
            <Checkbox on:click = {() => addProvince(found_province)}> Add</Checkbox>
        {/each}

        <Button on:click={()=> createCountry()}>Create country</Button>
        {#if display_result}
        <p>Change the tags to {tag} in the "history/provinces/provincefile" of those files:
            {#each provinces_toadd as province}
                <p>{province}</p>
            {/each}
        </p>
        {/if}
    </div>
</main>
  
<style>

</style>

