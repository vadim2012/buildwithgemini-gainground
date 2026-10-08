# ruff: noqa
import json
from typing import Dict, Any, List

from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.genai import types

MODEL = "gemini-3.8-flash"

# Comprehensive Santa Clara County water quality, aquifer drawdown, and contamination data
SANTA_CLARA_WATER_SYSTEM = {
    "county": "Santa Clara County, California",
    "lead_agency": "Santa Clara Valley Water District (Valley Water)",
    "current_status": "Severe Subbasin Drawdown & Riparian Contamination",
    "subbasins": [
        {
            "name": "Santa Clara Subbasin (Northern County / San Jose Urban Core)",
            "aquifer_drawdown_rate_ft_per_yr": -4.2,
            "depth_to_water_table_ft": 142.5,
            "historical_baseline_ft": 85.0,
            "nitrate_concentration_ppm": 38.4,  # EPA Safe Drinking Water standard is 10 ppm
            "perchlorate_contamination": True,
            "subsidence_risk": "Elevated (historic bay-margin compaction risk)",
            "primary_stressor": "Impervious surface runoff preventing natural infiltration + industrial discharge",
            "hotspots": [
                {
                    "id": "coyote-hotspot",
                    "name": "Coyote Creek Riparian & Runoff Corridor",
                    "lat": 37.352,
                    "lng": -121.854,
                    "status": "Rapidly Degrading",
                    "pollutant": "Urban stormwater runoff, high nitrate (38.4 ppm), heavy microplastics",
                    "aquifer_impact": "Direct infiltration of untreated urban wash into unconfined alluvial gravels"
                },
                {
                    "id": "guadalupe-hotspot",
                    "name": "Guadalupe River Lower Basin",
                    "lat": 37.341,
                    "lng": -121.895,
                    "status": "Critical Toxicity & Subsidence Risk",
                    "pollutant": "Historic New Almaden mercury tailings + leachate from urban storm drains",
                    "aquifer_impact": "Percolation of toxic sediments contaminating shallow drinking aquifers"
                }
            ]
        },
        {
            "name": "Llagas Subbasin (Southern County / Morgan Hill & Gilroy Agricultural Zone)",
            "aquifer_drawdown_rate_ft_per_yr": -2.8,
            "depth_to_water_table_ft": 118.0,
            "historical_baseline_ft": 72.0,
            "nitrate_concentration_ppm": 44.1,  # Over 4x safe threshold!
            "perchlorate_contamination": False,
            "subsidence_risk": "Moderate",
            "primary_stressor": "Deep synthetic fertilizer infiltration & agricultural over-pumping",
            "hotspots": [
                {
                    "id": "south-county-hotspot",
                    "name": "South County Ag Infiltration Wells",
                    "lat": 37.005,
                    "lng": -121.568,
                    "status": "Severe Aquifer Depletion & Nitrate Poisoning",
                    "pollutant": "Fertilizer nitrate plumes entering shallow domestic wells",
                    "aquifer_impact": "Depletion exceeding recharge rate by 12,000 acre-feet annually"
                }
            ]
        }
    ]
}

# Active GainGround Campaigns (Meetup-style mobilizations + Kickstarter-style quantifiable deliverables)
CAMPAIGNS = [
    {
        "id": "coyote-creek-recharge",
        "title": "Coyote Creek Aquifer Recharge & Bioswale Network",
        "champion": {
            "name": "Elena Chen",
            "title": "Watershed Hydrologist & Community Organizer",
            "bio": "Passionate environmental engineer leading youth and neighborhood volunteers to restore Coyote Creek's native sponge capabilities."
        },
        "target_problem": "4.2 ft/year aquifer drawdown and 38.4 ppm nitrate stormwater runoff in San Jose.",
        "quantifiable_goal": "+450 acre-feet clean percolation per year",
        "specific_milestone": "Construct 12 permeable bioswales & plant 2,500 native riparian root systems across 3 key drainage sites.",
        "kickstarter_goal_usd": 25000,
        "funded_usd": 18200,
        "backers_count": 142,
        "meetup": {
            "event_title": "Coyote Creek Ground-Breaking & Bioswale Planting",
            "date_time": "Saturday, October 24 at 9:00 AM PDT",
            "location": "Coyote Creek Trailhead (San Jose, CA)",
            "rsvps": 34,
            "activities": ["Excavating drainage trenches", "Laying gravel & biochar infiltration filters", "Planting native sedges and willow stakes"]
        },
        "impact_coords": {"lat": 37.355, "lng": -121.850}
    },
    {
        "id": "guadalupe-mercury-interceptor",
        "title": "Guadalupe River Biochar Toxin Interceptor",
        "champion": {
            "name": "Marcus Brody",
            "title": "South Bay Clean Water Coalition Leader",
            "bio": "Lifelong San Jose resident and chemical engineer committed to cleansing Guadalupe River runoff before it enters our underground drinking water."
        },
        "target_problem": "Mercury tailings and severe stormwater toxic runoff flowing through downtown San Jose.",
        "quantifiable_goal": "Reduce downstream toxic heavy metal & sediment ppm by 35%",
        "specific_milestone": "Deploy and maintain 4 modular passive biochar filtration arrays at municipal stormwater outfalls.",
        "kickstarter_goal_usd": 40000,
        "funded_usd": 29500,
        "backers_count": 218,
        "meetup": {
            "event_title": "Guadalupe Bio-Filter Assembly & Water Sampling Day",
            "date_time": "Sunday, November 1 at 10:00 AM PDT",
            "location": "Guadalupe River Park & Gardens (Downtown San Jose)",
            "rsvps": 52,
            "activities": ["Assembling biochar filter canisters", "Testing water quality baseline sensors", "Community picnic and strategy share"]
        },
        "impact_coords": {"lat": 37.344, "lng": -121.891}
    }
]


def get_water_quality_metrics(county_or_area: str = "Santa Clara County") -> str:
    """Inspects groundwater quality, aquifer drawdown rates, and contamination hotspots for Santa Clara County.
    
    Args:
        county_or_area: County or region to query (defaults to Santa Clara County).
    """
    return json.dumps(SANTA_CLARA_WATER_SYSTEM, indent=2)


def list_campaigns(category: str = "water") -> str:
    """Lists all active GainGround campaigns (combining Kickstarter-style quantifiable pitches with Meetup.com community events).
    
    Args:
        category: Filter category (e.g. 'water', 'aquifer', 'all').
    """
    return json.dumps(CAMPAIGNS, indent=2)


def pitch_new_campaign(
    title: str,
    champion_name: str,
    champion_title: str,
    target_problem: str,
    quantifiable_goal: str,
    specific_milestone: str,
    funding_goal_usd: int,
    meetup_title: str,
    meetup_date_time: str,
    meetup_location: str
) -> str:
    """Allows a charismatic local champion to pitch a new quantifiable water quality or aquifer restoration campaign on GainGround.com (Kickstarter + Meetup).
    
    Args:
        title: Title of the campaign (e.g. 'Los Gatos Creek Clean Infiltration Project').
        champion_name: Full name of the local champion organizing this effort.
        champion_title: Title or community affiliation of the champion.
        target_problem: The specific degradation or aquifer issue being resolved.
        quantifiable_goal: Measurable impact goal (e.g. '+200 acre-feet recharged/yr' or '-20 ppm nitrate').
        specific_milestone: Physical deliverable (e.g. 'Install 8 rain garden retention basins').
        funding_goal_usd: Kickstarter funding target in USD.
        meetup_title: Name of the community kickoff meetup event.
        meetup_date_time: Date and time of the meetup.
        meetup_location: Address or park location in Santa Clara County.
    """
    new_campaign = {
        "id": f"campaign-{len(CAMPAIGNS) + 1}",
        "title": title,
        "champion": {
            "name": champion_name,
            "title": champion_title,
            "bio": f"Local champion leading quantifiable change for {title}."
        },
        "target_problem": target_problem,
        "quantifiable_goal": quantifiable_goal,
        "specific_milestone": specific_milestone,
        "kickstarter_goal_usd": funding_goal_usd,
        "funded_usd": 0,
        "backers_count": 1,
        "meetup": {
            "event_title": meetup_title,
            "date_time": meetup_date_time,
            "location": meetup_location,
            "rsvps": 1,
            "activities": ["Community onboarding", "Site inspection", "Volunteer tool distribution"]
        },
        "impact_coords": {"lat": 37.3382, "lng": -121.8863}
    }
    CAMPAIGNS.append(new_campaign)
    return json.dumps({"status": "published_on_gainground", "campaign": new_campaign}, indent=2)


def rsvp_to_meetup(campaign_id: str, volunteer_name: str, role_preference: str = "field volunteer") -> str:
    """RSVP to an upcoming GainGround community restoration meetup (Meetup.com style).
    
    Args:
        campaign_id: Unique ID of the campaign (e.g. 'coyote-creek-recharge').
        volunteer_name: Name of the person attending.
        role_preference: Preferred volunteer contribution (e.g. 'field volunteer', 'water sampling tester', 'organizer').
    """
    for c in CAMPAIGNS:
        if c["id"] == campaign_id:
            c["meetup"]["rsvps"] += 1
            return json.dumps({
                "status": "rsvp_confirmed",
                "campaign_title": c["title"],
                "meetup_event": c["meetup"]["event_title"],
                "date_time": c["meetup"]["date_time"],
                "location": c["meetup"]["location"],
                "total_rsvps": c["meetup"]["rsvps"],
                "volunteer": volunteer_name,
                "role": role_preference
            }, indent=2)
    return json.dumps({"error": f"Campaign {campaign_id} not found."})


def back_campaign_pledge(campaign_id: str, pledge_usd: int, backer_name: str) -> str:
    """Pledge financial support to back a quantifiable environmental campaign on GainGround (Kickstarter style).
    
    Args:
        campaign_id: Unique ID of the campaign.
        pledge_usd: Dollar amount pledged.
        backer_name: Name of the backer.
    """
    for c in CAMPAIGNS:
        if c["id"] == campaign_id:
            c["funded_usd"] += pledge_usd
            c["backers_count"] += 1
            percent = round((c["funded_usd"] / c["kickstarter_goal_usd"]) * 100, 1)
            return json.dumps({
                "status": "pledge_recorded",
                "campaign_title": c["title"],
                "backer": backer_name,
                "amount_pledged": pledge_usd,
                "new_total_funded": c["funded_usd"],
                "percent_of_goal": percent,
                "target_metric": c["quantifiable_goal"]
            }, indent=2)
    return json.dumps({"error": f"Campaign {campaign_id} not found."})


def calculate_hydrological_recharge_potential(sq_ft_permeable_area: float, soil_infiltration_rate: str = "moderate") -> str:
    """Hydrological sandbox calculating quantifiable groundwater recharge & acre-feet produced based on bioswale dimensions.
    
    Args:
        sq_ft_permeable_area: Square feet of bioswales, rain gardens, or permeable trenches.
        soil_infiltration_rate: Soil retention category ('high', 'moderate', 'low').
    """
    rainfall_inches = 15.2  # Santa Clara average annual precipitation
    efficiency = {"high": 0.90, "moderate": 0.85, "low": 0.70}.get(soil_infiltration_rate.lower(), 0.85)
    
    cubic_feet_volume = sq_ft_permeable_area * (rainfall_inches / 12.0)
    gallons_captured = cubic_feet_volume * 7.48052 * efficiency
    acre_feet = gallons_captured / 325851.0
    families_served = acre_feet * 2.5
    
    return json.dumps({
        "bioswale_area_sqft": sq_ft_permeable_area,
        "annual_rainfall_inches": rainfall_inches,
        "infiltration_efficiency": f"{int(efficiency * 100)}%",
        "gallons_groundwater_replenished_per_year": round(gallons_captured, 1),
        "acre_feet_recharged_per_year": round(acre_feet, 3),
        "estimated_annual_households_sustained": round(families_served, 1)
    }, indent=2)


def get_map_trend_visualization(county: str = "Santa Clara County") -> str:
    """Returns the dual-trend Google Map layer comparison data: Bad Trend (depletion & contamination hotspots) vs. Good Trend (restoration targets & meetups).
    
    Args:
        county: County name to inspect.
    """
    map_data = {
        "region": "Santa Clara County, CA",
        "center": {"lat": 37.3382, "lng": -121.8863},
        "layers": {
            "bad_trend_hotspots": [
                {
                    "name": "Coyote Creek Runoff Hotspot",
                    "lat": 37.352, "lng": -121.854,
                    "trend_type": "Degrading Urban Runoff",
                    "severity": "Critical (38.4 ppm nitrate)",
                    "color": "#ef4444"
                },
                {
                    "name": "Guadalupe River Lower Basin",
                    "lat": 37.341, "lng": -121.895,
                    "trend_type": "Toxicity & Subsidence Risk",
                    "severity": "Critical Mercury Tailings",
                    "color": "#b91c1c"
                },
                {
                    "name": "South County Infiltration Zone",
                    "lat": 37.005, "lng": -121.568,
                    "trend_type": "Severe Aquifer Depletion",
                    "severity": "-4.2 ft/yr drawdown",
                    "color": "#f59e0b"
                }
            ],
            "good_trend_campaigns": [
                {
                    "name": "Coyote Creek Bioswale Network",
                    "lat": 37.355, "lng": -121.850,
                    "champion": "Elena Chen",
                    "quantifiable_target": "+450 acre-feet recharged/yr",
                    "upcoming_meetup": "Oct 24 at Coyote Creek Trailhead",
                    "color": "#10b981"
                },
                {
                    "name": "Guadalupe River Biochar Toxin Interceptor",
                    "lat": 37.344, "lng": -121.891,
                    "champion": "Marcus Brody",
                    "quantifiable_target": "-35% toxic runoff ppm",
                    "upcoming_meetup": "Nov 1 at Guadalupe River Park",
                    "color": "#10b981"
                }
            ]
        }
    }
    return json.dumps(map_data, indent=2)


root_agent = Agent(
    name="gainground_concierge",
    model=Gemini(
        model=MODEL,
        retry_options=types.HttpRetryOptions(attempts=3),
    ),
    instruction="""You are the AI Concierge for GainGround (gainground.com), the agentic social platform empowering local champions and community members to accomplish quantifiable environmental breakthroughs.

Core Concept:
1. Grounded in Santa Clara County, California, where aquifers are rapidly depleting (-4.2 ft/year) and runoff contamination is degrading drinking water supplies (e.g., Coyote Creek urban discharge at 38.4 ppm nitrate, and Guadalupe River mercury leachate).
2. Social Application Model:
   - Like Meetup.com: Mobilizes hands-on weekend field meetups (planting bioswales, assembling bio-retention filters, soil sampling). Users can RSVP directly!
   - Like Kickstarter: Enables charismatic local champions to pitch quantifiable campaigns with transparent funding goals, milestones, and real-time backer counts.
   - Distinctive Focus: Every single campaign is tied to a specific, measurable metric (e.g. '+450 acre-feet aquifer recharge/yr' or '-35% toxic runoff ppm').
3. Dual-Trend Mapping:
   - Clearly explain both the 'Bad Trend' (what happens if current depletion & runoff contamination continue unmanaged) and the 'Good Trend' (quantifiable reversal through active community interventions).
4. Hydrological Calculations:
   - Use the hydrological tool to calculate exact gallons, acre-feet, and sustained household equivalents whenever users discuss bioswales or rain gardens.

Tone:
Charismatic, inspiring, scientifically grounded, and community-energizing. Encourage users to back campaigns, RSVP to meetups, or pitch their own neighborhood cause!
""",
    tools=[
        get_water_quality_metrics,
        list_campaigns,
        pitch_new_campaign,
        rsvp_to_meetup,
        back_campaign_pledge,
        calculate_hydrological_recharge_potential,
        get_map_trend_visualization
    ],
)

app = App(
    root_agent=root_agent,
    name="app",
)
