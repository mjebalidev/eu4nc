<script>
import { Label, Input, Button, Dropdown, DropdownItem, Chevron ,Search, Checkbox, Hr} from 'flowbite-svelte'
import provinces_filelist from '../lib/provinces_list.txt'
import ColorPicker from 'svelte-awesome-color-picker';

let display_result = false

// tag
let tag = "ZAA" // 3 letters
let country_name = "Zaaland" // global
// global
let gouvernements = ["stateless_society","pirate_government","pirate_kingdom","holy_roman_electors_monarchy","holy_roman_electors_republic","japanese_shogunate","french_kingdom","default_monarchy","default_republic","default_theocracy","default_tribal","gov_steppe_horde","gov_native_council","noble_republic","gov_republican_dictatorship","gov_papal_government","gov_tribal","germanic_monastic_order","brewing_order","jewish_theocracy","zoroastrian_theocracy","orthodox_theocracy"]
let religions = ["ibadi","shiite","sunni","coptic","reformed","protestant","hussite","anglican","catholic","orthodox","paganism","jewish","zoroastrianism","buddhism","hinduism","islam","jainism","sikhism","shinto","taoism","confucianism","totemism","shamanism","animism"]
let cultures = ["pommeranian","prussian","baltic_german","lower_saxon","hannoverian","hessian","saxon","franconian","swabian","swiss","bavarian","austrian","dutch","flemish","frisian","swedish","danish","norwegian","finnish","sapmi","karelian","icelandic","norse","english","american","welsh","cornish","scottish","irish","highland_scottish","lombard","tuscan","sardinian","romagnan","ligurian","venetian","dalmatian","neapolitan","piedmontese","umbrian","sicilian","maltese","castillian","mexican","platinean","leonese","aragonese","catalan","galician","andalucian","portugese","brazilian","basque","cosmopolitan_french","gascon","normand","aquitaine","burgundian","breton"]
let graphical_cultures = []
let game_points = [1,2,3,4,5,6]

// history - countries - ZAA
let gouvernement = "monarchy"
let add_government_reform = "feudalism_reform"
let primary_culture = "prussian"
let religion = "catholic"
let elector = "no"
let capital = "50 # Berlin"
let technology_group = "western"
let add_accepted_culture = "sorbian"
let change_estate_land_share = " estate = estate_burghers share = -5 "
let monarch_name = "Tester"
let monarch_dynastie = "of Testenburg"
let monarch_adm = 6
let monarch_dip = 6
let monarch_mil = 6
let monarch_birth_date = "1423.1.1"
let monarch_religion = "catholic"
let monarch = `{ name = "${monarch_name}" dynasty = "${monarch_dynastie}" birth_date = ${monarch_birth_date} adm = ${monarch_adm} dip = ${monarch_dip} mil = ${monarch_mil} religion = ${monarch_religion} }`

// common - countries - ZAA
let graphical_culture = "westerngfx"
let rgb; // or hsv or hex
let picked_color = "Country color"
let color = "{ 161  139  40 }"
let revolutionnary_colors = "{ 0  4  15 }"
let color_elements = ["Country color", "Revolutionnary Country color"]
let prefered_religion = "protestant"
let historical_idea_groups = `
	economic_ideas
	defensive_ideas
	diplomatic_ideas
	offensive_ideas
	innovativeness_ideas
	quantity_ideas
	administrative_ideas
	religious_ideas
`
let historical_units = `
	western_medieval_infantry
	western_medieval_knights
	western_men_at_arms
	swiss_landsknechten
	dutch_maurician
	austrian_tercio
	austrian_grenzer
	austrian_hussar
	austrian_white_coat
	austrian_jaeger
	mixed_order_infantry
	open_order_cavalry
	napoleonic_square
	napoleonic_lancers
`
let monarch_names = `
    "Vratislav #3" = 5
	"Boleslav #4" = 10
	"Viktor #0" = 0
	"Jaroslav #0" = 1
	"Anezka #0" = -1
	"Eliska #0" = -1
	"Katerina #0" = -1
	"Marie #0" = -1
	"Ludmila #0" = -1
	"Alzbeta #0" = -1
`
let leader_names = `
    "z Otradovic"
	"z Falkensteina"
`
let ship_names = `
    Orel
	Sokol
	Slezsko
	Sipka
	Hvezda
`


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
    let countries_00_tag = `${tag} = "countries/${country_name}.txt"`
    monarch = `{ name = "${monarch_name}" dynasty = "${monarch_dynastie}" birth_date = ${monarch_birth_date} adm = ${monarch_adm} dip = ${monarch_dip} mil = ${monarch_mil} religion = ${monarch_religion} }`

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
    change_estate_land_share = {${change_estate_land_share}}
    1444.1.1 = { 
        monarch = {${monarch}}
    }
    `

    // common/countries/ZAA - ZAAcustom.txt
    let end_common_countries = `
    graphical_culture = ${graphical_culture}
    color = ${color}
    revolutionnary_colors = ${revolutionnary_colors}
    prefered_religion = ${prefered_religion}
    historical_idea_groups = {${historical_idea_groups}}
    historical_units = {${historical_units}}
    monarch_names = {${monarch_names}}
    leader_names = {${leader_names}}
    ship_names = {${ship_names}}
    `

    //localisation files
    let countries_l_english_content = `
    l_english: 
    ${tag}:0 "${country_name}"
    ${tag}_ADJ:0 "${country_name}"
    `
    let countries_l_french_content = `
    l_french: 
    ${tag}:0 "${country_name}"
    ${tag}_ADJ:0 "${country_name}"
    `
    // provinces
    // provinces_toadd

    downloadFile("YOURMODNAME_countries.txt",countries_00_tag)
    downloadFile(tag + " - " + country_name + ".txt",end_history_countries)
    downloadFile(country_name + ".txt",end_common_countries)
    downloadFile("countries_l_english.yml", countries_l_english_content)
    downloadFile("countries_l_french.yml", countries_l_french_content)
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
    link.download = name;
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
        <Button color="dark"><Chevron>Government: {gouvernement}</Chevron></Button>
        <Dropdown >
        {#each gouvernements as selected_gouvernement}
            <DropdownItem on:click={()=> gouvernement=selected_gouvernement} >{selected_gouvernement}</DropdownItem>
        {/each}
        </Dropdown>
        <!-- 
        <Label>Government reform</Label>
        <Input bind:value={add_government_reform} />
        -->        
        <Button color="dark"><Chevron>Primary culture: {primary_culture}</Chevron></Button>
        <Dropdown >
        {#each cultures as selected_culture}
            <DropdownItem on:click={()=> primary_culture=selected_culture} >{selected_culture}</DropdownItem>
        {/each}
        </Dropdown>
        <Button color="dark"><Chevron>Religion: {religion}</Chevron></Button>
        <Dropdown >
        {#each religions as selected_religion}
            <DropdownItem on:click={()=> religion=selected_religion} >{selected_religion}</DropdownItem>
        {/each}
        </Dropdown>
        <!-- 
        <Label>Elector</Label>
        <Input bind:value={elector} />
         -->
        <Label>Capital</Label>
        <Input bind:value={capital} />
        <Label>Technology group</Label>
        <Input bind:value={technology_group} />
        <Label>Accepted culture</Label>
        <Input bind:value={add_accepted_culture} />
        <!-- 
        <Label>Change estate land share</Label>
        <Input bind:value={change_estate_land_share} />
         -->

        <Hr/>
        <Label>Monarch name</Label>
        <Input bind:value={monarch_name} />
        <Label>Monarch dynastie</Label>
        <Input bind:value={monarch_dynastie} />

        <Button color="dark"><Chevron>Monarch ADM: {monarch_adm}</Chevron></Button>
        <Dropdown >
        {#each game_points as game_point}
            <DropdownItem on:click={()=> monarch_adm=game_point} >{game_point}</DropdownItem>
        {/each}
        </Dropdown>

        <Button color="dark"><Chevron>Monarch DIP: {monarch_dip}</Chevron></Button>
        <Dropdown >
        {#each game_points as game_point}
            <DropdownItem on:click={()=> monarch_dip=game_point} >{game_point}</DropdownItem>
        {/each}
        </Dropdown>

        <Button color="dark"><Chevron>Monarch MIL: {monarch_mil}</Chevron></Button>
        <Dropdown >
        {#each game_points as game_point}
            <DropdownItem on:click={()=> monarch_mil=game_point} >{game_point}</DropdownItem>
        {/each}
        </Dropdown>
        <!-- 
        <Label>Monarch birth date</Label>
        <Input bind:value={monarch_birth_date} />
         -->
        <Button color="dark"><Chevron>Monarch religion: {monarch_religion}</Chevron></Button>
        <Dropdown >
        {#each religions as selected_religion}
            <DropdownItem on:click={()=> monarch_religion=selected_religion} >{selected_religion}</DropdownItem>
        {/each}
        </Dropdown>
        <Hr/>
        <Label>Graphical culture</Label>
        <Input bind:value={graphical_culture} />
        <Label>Color:</Label> <p>{color}</p>
        <Label>Revolutionnary Color:</Label> <p>{revolutionnary_colors}</p>
        <Button color="dark"><Chevron>Selected color: {picked_color}</Chevron></Button>
        <Dropdown >
        {#each color_elements as color}
            <DropdownItem on:click={()=> picked_color = color } >{color}</DropdownItem>
        {/each}
        </Dropdown>
        <ColorPicker on:input = {() => {

            if (picked_color == "Country color"){
            color = "{ " + rgb.r + " " + rgb.g + " " + rgb.b + " }"
            }
            else if (picked_color == "Revolutionnary Country color"){
            revolutionnary_colors = "{ " + rgb.r + " " + rgb.g + " " + rgb.b + " }"
            }

            console.log(rgb)
            console.log(picked_color)
            }} bind:rgb />
        <!-- 
        <Label>Prefered religion</Label>
        <Input bind:value={prefered_religion} />
        <Label>Historical idea groups</Label>
        <Input bind:value={historical_idea_groups} />
        <Label>Historical units</Label>
        <Input bind:value={historical_units} />
         -->
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
        <Hr/>
        <Button color="yellow" on:click={()=> createCountry()}>Create country</Button>
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

