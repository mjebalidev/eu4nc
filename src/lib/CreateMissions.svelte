<script>

    import { Label, Range, Table, TableBody, TableBodyCell, TableBodyRow, TableHead, TableHeadCell } from 'flowbite-svelte';
    
    let minmaxValue=2
    let missions = Array.from({ length: minmaxValue }, (_, i) => `item ${i + 1}`);
    console.log(missions)
    function createMission(){

    }

    function renderTableList(){
        missions = Array.from({ length: minmaxValue }, (_, i) => `item ${i + 1}`);
        console.log(missions)
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
    <div>
        <Label>Min-max range</Label>
        <Range id="range-minmax" min="0" max="10" on:change={renderTableList} bind:value={minmaxValue}/>
        <p>Value: {minmaxValue}</p>
        <Table>
            <TableHead>
                <TableHeadCell>Name of the mission</TableHeadCell>
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
            {#each missions as mission}
                <TableBody>
                    <TableBodyRow>
                        <TableBodyCell><span contenteditable="true" >missions</span></TableBodyCell>
                        <TableBodyCell><span contenteditable="true" >slot</span></TableBodyCell>
                        <TableBodyCell><span contenteditable="true" >generic</span></TableBodyCell>
                        <TableBodyCell><span contenteditable="true" >ai</span></TableBodyCell>
                        <TableBodyCell><span contenteditable="true" >has_country_shield</span></TableBodyCell>
                        <TableBodyCell><span contenteditable="true" >potential_on_load</span></TableBodyCell>
                        <TableBodyCell><span contenteditable="true" >potential</span></TableBodyCell>
                        <TableBodyCell><span contenteditable="true" >icon</span></TableBodyCell>
                        <TableBodyCell><span contenteditable="true" >position</span></TableBodyCell>
                        <TableBodyCell><span contenteditable="true" >completed_by</span></TableBodyCell>
                    </TableBodyRow>
                </TableBody>
            {/each}
        </Table>
    </div>
</main>
  
<style>

</style>