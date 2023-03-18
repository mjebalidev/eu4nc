<script>

    import { Button, Input, Label, Range, Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
    let value = ""
    let minmaxValue=2
    let json_container = []

    let missions = Array.from({ length: minmaxValue }, (_, i) => `{"key": ${i + 1}, "slot": "", "mission": "test", "generic": false, "ai": false, "has_country_shield": false, "potential_on_load": "", "potential": "", "icon": "", "position": 0, "completed_by": "", "required_missions": "", "trigger": "", "effect": ""}`);
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
            <trigger>
        }
        
        # Determines when a series appears for a country. Country scope.
        potential = {
            <trigger>
        }
        
        # The name of the mission, used for localization
        ${json_container[i].mission} = {
            icon = <gfx>            # The icon to use for the mission, without the file extension.
            position = ${json_container[i].position}        # Which row the mission appears in. 1 is top. If you omit this line, it will occupy the first row aviable.
            completed_by = ${json_container[i].completed_by}   # Automatically completes mission in that date. Can also give this mission a non in-game date (like "1999.11.11") to never make them completing automatically.
            
            # Which missions must be completed before this mission is active.
            required_missions = {
                ${json_container[i].required_missions}
            }
            
            # Determines which provinces to highlight. Acts like all_province scope. Optional.
            provinces_to_highlight = {
                <trigger>
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
        for(let i = 0; i < minmaxValue; i++){
            json_container[i] = JSON.parse(missions[i])
        }
        console.log(missions)
    }

    function printData(){
        console.log(json_container[0])
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
    <div class="main-frame">
        <Label>Min-max range</Label>
        <Range id="range-minmax" min="0" max="10" on:change={renderTableList} bind:value={minmaxValue}/>
        <p>Value: {minmaxValue}</p>
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
                        <TableBodyCell><Input class="w-full" bind:value={mission.slot}/></TableBodyCell>
                        <TableBodyCell><Input class="w-full" bind:checked={mission.generic}/></TableBodyCell>
                        <TableBodyCell><Input bind:checked={mission.ai}/></TableBodyCell>
                        <TableBodyCell><Input bind:checked={mission.has_country_shield}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.potential_on_load}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.potential}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.icon}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.position}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.completed_by}/></TableBodyCell>
                        <TableBodyCell><Input bind:value={mission.required_missions}/></TableBodyCell>
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