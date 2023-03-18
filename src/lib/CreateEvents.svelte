<script>
    let event = {
    id: 0,
    title: "",
    desc: "",
    picture: "",
    fire_only_once: false
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

    </div>
</main>
  
<style>

</style>