<script>

    import { Hr, Chevron, Dropdown, DropdownItem, Button, Input, Label, Range, Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell, Checkbox } from 'flowbite-svelte';
    let value = ""
    let minmaxValue=2
    let json_container = []
    let boolean_container = ["true", "false"]
    let slot_number = [1,2,3,4,5]
    let mission_icons = ['mission_dominate_home_trade_node', 'mission_egyptian_mamluk_soldier', 'mission_kowtow', 'mission_conquer_5_states', 'mission_iberian_conquistador', 'mission_asian_city', 'mission_early_modern_university', 'mission_bedouins', 'mission_iroquois_warriors', 'mission_junk_boat', 'mission_chinese_general_riding', 'mission_sw_yucca_plants', 'mission_japanese_fort', 'mission_asian_trader', 'mission_indian_soldier_elephant', 'mission_arabian_fort', 'mission_religious', 'mission_steppe_warriors', 'oceania_assemble_an_army', 'mission_hanseatic_city', 'mission_non-western_soldiers', 'mission_hands_praying', 'mission_buddhist_monk_praying', 'mission_crusade_for_varna', 'mission_central_asian_city', 'mission_african_soldier', 'mission_persian_soldiers', 'mission_empire', 'mission_teutonic_knights', 'mission_ne_palisades', 'oceania_royal_marriage', 'mission_assemble_an_army', 'mission_alliances', 'mission_galleys_in_port', 'mission_rice_field', 'mission_market_place_with_asian_traders', 'mission_sw_torquoise_mining', 'mission_se_medicine_wheel', 'mission_cossack_cavalry', 'mission_indian_stateman', 'ne_agriculture', 'mission_trigger', 'polynesian_navy_build', 'mission_mosque', 'native_royal_marriage', 'mission_ne_birch_bark_canoes', 'se_platform_mounds', 'se_along_the_river', 'mission_luther_theses', 'mission_japanese_samurai', 'mission_monarch_in_throne_room', 'mission_italian_condottiere', 'control_unrest', 'polynesian_grand_navy', 'mission_impaled_soldies', 'native_build_army_mission', 'mission_war_chest', 'mission_asian_cannon', 'mission_invade_island', 'mission_sea_battles', 'mission_colonial', 'mission_early_game_buildings', 'mission_sw_against_the_desert', 'mission_settlers_north_america', 'mission_trade_company_region_abroad', 'mission_scholar_officials', 'mission_cannons_firing', 'oceania_dev_capital', 'mission_conquer_50_development', 'mission_noble_council', 'mission_have_manufactories', 'mission_high_income', 'mission_have_two_subjects', 'mission_se_birdmen', 'ne_great_lakes_conquest', 'mission_ottoman_harem', 'oceania_build_army_mission', 'mission_non-western_cavalry_raid', 'native_dev_capital', 'mission_great_wall', 'mission_eastern_european_city', 'mission_manchu_warrior', 'mission_unite_home_region', 'mission_establish_high_seas_navy', 'ne_longhouses', 'gain_mana', 'mission_european_church', 'mission_build_up_to_force_limit', 'mission_landsknecht_soldier'];

    let missions = Array.from({ length: minmaxValue }, (_, i) => `{"key": ${i + 1}, "slot": "1 to 5", "mission": "my mission name ${i+1}", "generic": false, "ai": false, "has_country_shield": false, "potential_on_load": "", "potential": "", "icon": "", "position": 0, "completed_by": "", "required_missions": "", "trigger": "", "effect": ""}`);
    for(let i = 0; i < minmaxValue; i++){
        json_container[i] = JSON.parse(missions[i])
    }
    console.log(json_container[0].key)

    let mission_name = ""
    let mission_generic = ""
    let mission_ai = ""
    let mission_has_country_shield = ""
    let mission_potential_on_load = ""
    let mission_potential = ""
    let mission_icon = ""
    let mission_position = ""
    let mission_completed_by = ""
    let mission_required_missions = ""
    let mission_trigger = ""
    let mission_effect = ""
    let missions_data = ""
    let display_result = false


    function createMission(){
        // for each element in the array
        missions_data = ""
        for(let i=0; i<json_container.length; i++){
        // create mission
        let mission = `
        <series> = {
        slot = ${json_container[i].slot}                    # Which column the missions will appear in. 1 to 5.
        generic = ${json_container[i].generic}             # Whether missions within this series are considered generic.
        ai = ${json_container[i].ai}                  # Whether the AI will claim missions in this series.
        has_country_shield = ${json_container[i].has_country_shield}  # Whether to display the country shield on the icon.    
        
        # Determines whether a series is loaded at all. Used to limit series to DLC.
        potential_on_load = {
            ${json_container[i].potential_on_load}
        }
        
        # Determines when a series appears for a country. Country scope.
        potential = {
            ${json_container[i].potential}
        }
        
        # The name of the mission, used for localization
        ${json_container[i].mission} = {
            icon = ${json_container[i].icon}            # The icon to use for the mission, without the file extension.
            position = ${json_container[i].position}        # Which row the mission appears in. 1 is top. If you omit this line, it will occupy the first row aviable.
            completed_by = ${json_container[i].completed_by}   # Automatically completes mission in that date. Can also give this mission a non in-game date (like "1999.11.11") to never make them completing automatically.
            
            # Which missions must be completed before this mission is active.
            required_missions = {
                ${json_container[i].required_missions}
            }
            
            # Determines which provinces to highlight. Acts like all_province scope. Optional.
            provinces_to_highlight = {
                ${json_container[i].provinces_to_highlight}
            }
        
            # Determines when the mission is completed. Country scope.
            trigger = {
                ${json_container[i].trigger}
            }
            
            # The effect executed when the mission is claimed. Country scope.
            effect = {
                ${json_container[i].effect}
            }
            }
        }
        `
        missions_data = missions_data + mission
        }
        console.log(missions_data)
        display_result = true
        downloadFile("missions", missions_data)
    }

    function renderTableList(){
        let missions = Array.from({ length: minmaxValue }, (_, i) => `{"key": ${i + 1}, "slot": "", "mission": "test", "generic": false, "ai": false, "has_country_shield": false, "potential_on_load": "", "potential": "", "icon": "", "position": 0, "completed_by": "", "required_missions": "", "trigger": "", "effect": ""}`);
        json_container = []
        for(let i = 0; i < minmaxValue; i++){
            json_container[i] = JSON.parse(missions[i])
        }
        console.log(missions)
    }

    function printData(){
        console.log(json_container[0])
    }

    function addRequiredMission(mission, required_mission){
        if(!mission.includes(required_mission)){
            mission = required_mission + "\n" + mission
        }
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
/*     
    <series> = {
    slot = <int>                    # Which column the missions will appear in. 1 to 5.
    generic = <boolean>             # Whether missions within this series are considered generic.
    ai = <boolean>                  # Whether the AI will claim missions in this series.
    has_country_shield = <boolean>  # Whether to display the country shield on the icon.    
    
    # Determines whether a series is loaded at all. Used to limit series to DLC.
    potential_on_load = {
        <trigger>
    }
    
    # Determines when a series appears for a country. Country scope.
    potential = {
        <trigger>
    }
    
    # The name of the mission, used for localization
    <mission> = {
        icon = <gfx>            # The icon to use for the mission, without the file extension.
        position = <int>        # Which row the mission appears in. 1 is top. If you omit this line, it will occupy the first row aviable.
        completed_by = <date>   # Automatically completes mission in that date. Can also give this mission a non in-game date (like "1999.11.11") to never make them completing automatically.
        
        # Which missions must be completed before this mission is active.
        required_missions = {
            <mission>
        }
        
        # Determines which provinces to highlight. Acts like all_province scope. Optional.
        provinces_to_highlight = {
            <trigger>
        }
    
        # Determines when the mission is completed. Country scope.
        trigger = {
            <trigger>
        }
        
        # The effect executed when the mission is claimed. Country scope.
        effect = {
            <effect>
        }
        }
    } 
*/

</script>
  
<main>
    <Label>Min-max range</Label>
    <Range id="range-minmax" min="1" max="20" on:change={renderTableList} bind:value={minmaxValue}/>
    <p>Value: {minmaxValue}</p>
    <Hr/>
    <div class="main-frame">
        <Table class="table">
            <TableHead>
                <TableHeadCell>Name of the mission</TableHeadCell>
                <TableHeadCell>Slot</TableHeadCell>
                <TableHeadCell>Generic</TableHeadCell>
                <TableHeadCell>AI</TableHeadCell>
                <TableHeadCell>Has Country Shield</TableHeadCell>
                <TableHeadCell>Potential On Load</TableHeadCell>
                <TableHeadCell>Potential</TableHeadCell>
                <TableHeadCell>Icon</TableHeadCell>
                <TableHeadCell>Position</TableHeadCell>
                <TableHeadCell>Completed By</TableHeadCell>
                <TableHeadCell>Required Missions</TableHeadCell>
                <TableHeadCell>Provinces To Highlight</TableHeadCell>
                <TableHeadCell>Trigger</TableHeadCell>
                <TableHeadCell>Effect</TableHeadCell>
            </TableHead>
            {#each json_container as mission}
                <TableBody>
                    <TableBodyRow>
                        <TableBodyCell><Input class="w-full" on:change={printData} bind:value={mission.mission}/></TableBodyCell>
                        <TableBodyCell>
                            <Button><Chevron>Slot: {mission.slot}</Chevron></Button>
                            <Dropdown >
                                {#each slot_number as number}
                                    <DropdownItem on:click={()=> mission.slot=number} >{number}</DropdownItem>
                                {/each}
                                </Dropdown>
                        </TableBodyCell>
                        
                        <TableBodyCell>
                            <Button><Chevron>Generic: {mission.generic}</Chevron></Button>
                            <Dropdown >
                            {#each boolean_container as boolean_choice}
                                <DropdownItem on:click={()=> mission.generic=boolean_choice} >{boolean_choice}</DropdownItem>
                            {/each}
                            </Dropdown>
                        </TableBodyCell>
                        <TableBodyCell>
                            <Button><Chevron>AI: {mission.ai}</Chevron></Button>
                            <Dropdown >
                            {#each boolean_container as boolean_choice}
                                <DropdownItem on:click={()=> mission.ai=boolean_choice} >{boolean_choice}</DropdownItem>
                            {/each}
                            </Dropdown>
                        </TableBodyCell>
                        <TableBodyCell>
                            <Button><Chevron>Has Country Shield: {mission.has_country_shield}</Chevron></Button>
                            <Dropdown >
                            {#each boolean_container as boolean_choice}
                                <DropdownItem on:click={()=> mission.has_country_shield = boolean_choice} >{boolean_choice}</DropdownItem>
                            {/each}
                            </Dropdown>
                        </TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.potential_on_load}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.potential}/></TableBodyCell>
                        <TableBodyCell>
                            <Button><Chevron>Icon: {mission.icon}</Chevron></Button>
                            <Dropdown >
                            {#each mission_icons as icon}
                                <DropdownItem on:click={()=> mission.icon = icon} >{icon}</DropdownItem>
                            {/each}
                            </Dropdown>
                        </TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.position}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.completed_by}/></TableBodyCell>
                        <TableBodyCell>
                            <Button><Chevron>Required missions: {mission.required_missions}</Chevron></Button>
                            <Dropdown >
                            {#each json_container as required_mission}
                                <li><Checkbox on:click={() => {
                                    if(!mission.required_missions.includes(required_mission.mission)){
                                    mission.required_missions = required_mission.mission + "\n" + mission.required_missions; 
                                    }
                                    console.log(mission.required_missions)
                                }
                                }>{required_mission.mission}</Checkbox></li>
                            {/each}
                            </Dropdown>
                        </TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.provinces_to_highlight}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.trigger}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.effect}/></TableBodyCell>
                    </TableBodyRow>
                </TableBody>
            {/each}
        </Table>
        <Button on:click={createMission}>Test</Button>
        {#if display_result}
            <p>{missions_data}</p>
        {/if}

    </div>
</main>
  
<style>
    .table-cell {
        width: 100px;
    }
    .main-frame {
        width: 150%;
        height: 100%;
        display: flex;
        flex-direction: column;
    }
</style>