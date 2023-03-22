<script>
	import { Secondary, Hr, Chevron, Dropdown, DropdownItem, Button, Input, Label, Range, Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox } from 'flowbite-svelte';

	let event_id = ""
	let event_title = ""
	let event_desc = ""
	let event_picture = "" // https://eu4.paradoxwikis.com/List_of_event_pictures
	let event_fire_only_once = "no"
	let event_major = "yes"
	let event_major_trigger = ""
	let event_option = ""
	let event_trigger = ""
	let event_types = ["country_event","province_event"]
	let events_names_underscore = []
	let yes_no = ["yes","no"]
	let event_type = event_types[0]
	let display_result = false

	let event = {
	event_type: event_type,
    id: event_id,
    title: event_title,
    desc: event_desc,
    picture: event_picture,
    fire_only_once: event_fire_only_once,
	major: event_major,
	major_trigger: event_major_trigger,
	trigger: event_trigger,
	option: event_option,
    }

	let events_l_english_content_temp = ""
	let events_l_english_content = ""
	let events_l_french_content_temp = ""
	let events_l_french_content = ""


	let json_container = []

	let minmaxValue=2

	let event_complete = ""

	let events = Array.from({ length: minmaxValue }, 
		(_, i) => 
		`{"key": ${i + 1},"event_type": "${event_type}", "id": ${i+1}, "title": "${event_title}", "desc": "${event_desc}", "picture": "${event_picture}", "fire_only_once": "${event_fire_only_once}", "major": "${event_major}", "major_trigger": "${event_major_trigger}","trigger": "${event_trigger}", "option": "${event_option}"}`);
	for(let i = 0; i < minmaxValue; i++){
        json_container[i] = JSON.parse(events[i])
    }

	function renderTableList(){
        events = Array.from({ length: minmaxValue }, 
		(_, i) => 
		`{"key": ${i + 1},"event_type": "${event_type}", "id": ${i+1}, "title": "${event_title}", "desc": "${event_desc}", "picture": "${event_picture}", "fire_only_once": "${event_fire_only_once}", "major": "${event_major}", "major_trigger": "${event_major_trigger}","trigger": "${event_trigger}", "option": "${event_option}"}`);
        json_container = []
        for(let i = 0; i < minmaxValue; i++){
            json_container[i] = JSON.parse(events[i])
        }
        console.log(json_container)
    }

	function downloadFile(name,file) {
        // Create a new file blob from the contents
        const fileBlob = new Blob([file], { type: 'text/plain' });

        // Create a URL for the file blob
        const fileUrl = URL.createObjectURL(fileBlob);

        // Create a new anchor element
        const link = document.createElement('a');

        // Set the download attribute and file URL
        link.download = name ;
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

	function createEvent(){
		let event_data = ""
		for(let i=0; i<json_container.length; i++){
			event_data = `
			${json_container[i].event_type} = {
				id = ${json_container[i].id}
				title = ${json_container[i].title}
				desc = ${json_container[i].desc}
				picture = ${json_container[i].picture}
				fire_only_once = ${json_container[i].fire_only_once}
				major = ${json_container[i].major}
				major_trigger = ${json_container[i].major_trigger}
				option = ${json_container[i].option}
			}
			`
			event_complete += event_data
			let event_name_underscore = json_container[i].title
            event_name_underscore = event_name_underscore.replace(/ /g, "_")
            events_names_underscore.push(event_name_underscore)
            //localisation files
            events_l_english_content_temp = ` 
            ${event_name_underscore}.t:0 "${json_container[i].title}"
            ${event_name_underscore}.d:0 "${json_container[i].desc}"
            `
            events_l_english_content = events_l_english_content + events_l_english_content_temp

            events_l_french_content_temp = `
            ${event_name_underscore}.t:0 "${json_container[i].title}"
            ${event_name_underscore}.d:0 "${json_container[i].desc}"
            `
            events_l_french_content = events_l_french_content + events_l_french_content_temp

		}

		


		console.log(event_complete)
		display_result = true
		downloadFile("events.txt", event_complete)
		downloadFile("events_l_english.yml", events_l_english_content)
        downloadFile("events_l_french.yml", events_l_english_content)
	}
/* 
#Hussites march on Prague
country_event = {
	id = flavor_boh.1
	title = flavor_boh.1.t
	desc = flavor_boh.1.d
	picture = {	
		trigger = {
			has_dlc = "Emperor"
		}
		picture = HUSSITE_eventPicture
	}
	picture = {	
		trigger = {
			NOT = { has_dlc = "Emperor" }
		}
		picture = CIVIL_WAR_eventPicture
	}

	fire_only_once = yes

	trigger = {
		tag = BOH
		owns = 266
		is_year = 1446
		NOT = { is_year = 1500 }
		is_at_war = no
		OR = {
			religion = catholic
			religion = hussite
		}
		is_free_or_tributary_trigger = yes
	}
	
	mean_time_to_happen = {
		months = 17
	}
	immediate = {
		hidden_effect = {
			set_country_flag = first_hussite_king
		}
	}
	
	option = { # Convert to Hussite
		ai_chance = { factor = 10 }
		name = flavor_boh.1.a
		set_country_flag = hussite_regency_mission_flag
		if = {
			limit = {
				has_regency = no
			}
			tooltip = {
				kill_ruler = yes
			}
		}
		if = {
			limit = {
				has_heir = yes
			}
			remove_heir = {}
		}
		change_religion = hussite
		define_ruler = {
			name = "Jir�"
			dynasty = "z Podebrad"
			adm = 5
			dip = 4
			mil = 3
			religion = hussite
			culture = czech
			age = 25
		}
		if = {
			limit = {
				has_states_general_mechanic = yes
			}
			change_statists_vs_orangists = 1
		}
		if = {
			limit = {
				has_dlc = "Rights of Man" 
			}
			hidden_effect = { add_ruler_personality_ancestor = { key = zealot } }
		}
		add_reform_desire = 0.02
	}
	
	option = { # Hussite King, Catholic nation - tolerance option
		ai_chance = { factor = 90 }
		set_country_flag = hussite_regency_mission_flag
		name = flavor_boh.1.c
		add_papal_influence = -100
		if = {
			limit = {
				has_regency = no
			}
			tooltip = {
				kill_ruler = yes
			}
		}
		if = {
			limit = {
				has_heir = yes
			}
			remove_heir = {}
		}
		define_ruler = {
			name = "Jir�"
			dynasty = "z Podebrad"
			adm = 5
			dip = 4
			mil = 3
			religion = hussite
		}
		if = {
			limit = {
				has_states_general_mechanic = yes
			}
			change_statists_vs_orangists = 1
		}
		add_reform_desire = 0.01
		add_ruler_modifier = {
			name = "boh_hussite_king"
			duration = -1
		}
		PAP = {
			country_event = { id = flavor_boh.9 }
		}
	}
	
	option = { # Fight them
		name = flavor_boh.1.b
		set_country_flag = hussite_regency_mission_flag
		266 = {
			spawn_rebels = {
				type = pretender_rebels
				size = 1
				leader = "Jir�"
				leader_dynasty = "z Podebrad"
			}		
		}
		random_owned_province = {
			limit = {
				NOT = { province_id = 266 }
			}
			spawn_rebels = {
				type = pretender_rebels
				size = 1
			}
		}
		if = {
			limit = { religion = catholic }
			add_papal_influence = 10
			PAP = {
				add_opinion = {
					who = root
					modifier = boh_papal_reconciled
				}
			}
		}
	}
}
 */
</script>
  
<main>
    <div>
		<Label> Events picture names: </Label>
		<Button outline color="yellow" href="https://eu4.paradoxwikis.com/List_of_event_pictures" target="_blank">Go to https://eu4.paradoxwikis.com/List_of_event_pictures</Button>
		
		<Hr/>
		<div>
			<Label>Number of events</Label> <p>{minmaxValue}</p>
			<Range id="range-minmax" min="1" max="20" on:change={renderTableList} bind:value={minmaxValue}/>
		</div>
		<div class="main-frame">
			<Table class="table">
				<TableHead>
					<TableHeadCell>Event type</TableHeadCell>
					<TableHeadCell>Event title</TableHeadCell>
					<TableHeadCell>Event description</TableHeadCell>
					<TableHeadCell>Event picture</TableHeadCell>
					<TableHeadCell>Fire only once</TableHeadCell>
					<TableHeadCell>Major</TableHeadCell>
					<TableHeadCell>Major Trigger</TableHeadCell>
					<TableHeadCell>Trigger</TableHeadCell>
					<TableHeadCell>Option</TableHeadCell>
				</TableHead>
				{#each json_container as event}
					<TableBody>
						<TableBodyRow>
							<TableBodyCell>
								<Button outline color="yellow"><Chevron>Type: {event.event_type}</Chevron></Button>
								<Dropdown >
								{#each event_types as type}
									<DropdownItem on:click={()=> event.event_type = type} >{type}</DropdownItem>
								{/each}
								</Dropdown>
							</TableBodyCell>
							<TableBodyCell><Input bind:value={event.title}/></TableBodyCell>
							<TableBodyCell><Input bind:value={event.desc}/></TableBodyCell>
							
							<TableBodyCell><Input bind:value={event.picture}/></TableBodyCell>
							<TableBodyCell>
								<Button outline color="yellow"><Chevron>Fire only once: {event.fire_only_once}</Chevron></Button>
								<Dropdown >
								{#each yes_no as choice}
									<DropdownItem on:click={()=> event.fire_only_once = choice} >{choice}</DropdownItem>
								{/each}
								</Dropdown>
							</TableBodyCell>
							<TableBodyCell>
								<Button outline color="yellow"><Chevron>Major: {event.major}</Chevron></Button>
								<Dropdown >
								{#each yes_no as choice}
									<DropdownItem on:click={()=> event.major = choice} >{choice}</DropdownItem>
								{/each}
								</Dropdown>
							</TableBodyCell>
							<TableBodyCell><Input bind:value={event.major_trigger}/></TableBodyCell>
							<TableBodyCell><Input bind:value={event.trigger}/></TableBodyCell>
							<TableBodyCell><Input bind:value={event.option}/></TableBodyCell>
						</TableBodyRow>
					</TableBody>
				{/each}
			</Table>
			<Hr/>
			<Button color="yellow" on:click={createEvent}>Render & Download</Button>
			{#if display_result}
				<p>{event_complete}</p>
			{/if}
	
		</div>
    </div>
</main>
  
<style>

</style>