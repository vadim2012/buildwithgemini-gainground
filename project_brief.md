# My agent: GainGround Concierge (gainground.com)
One-liner: A conversational and civic action agent that helps local community champions and residents pitch, fund, and mobilize campaigns around quantifiable local environmental goals (e.g., Santa Clara County groundwater & aquifer restoration) with interactive impact maps and crowdfunding project cards.

Tool coverage:
- Memory: Remembers user's home county/district, pinned campaigns, pledges/backed amounts, RSVP'd events, and skill interests (e.g. volunteer, organizer, funder).
- Tools:
  - `get_regional_metrics(county, metric_type)`: Fetches real/simulated environmental baseline data (e.g., Santa Clara Valley Water District aquifer levels, nitrate ppm, contamination hotspots).
  - `list_campaigns(county, category)`: Fetches active campaigns (meetups, Kickstarter-style pitches).
  - `generate_map_trend_overlay(county, trend_type)`: Generates GeoJSON/Google Maps configuration showing current degradation hotspots (bad trend) vs. targeted remediation zones (good trend).
  - `pitch_campaign(...)`: Allows a local champion to scaffold a new quantifiable initiative with milestones and funding tiers.
- Catalog/UI:
  - Campaign Cards: Goal progress bars, champion profile, target metrics (e.g., "+15% aquifer recharge by Q4"), meeting location, RSVP/pledge buttons.
  - Metrics & Hotspot Table: Breakdown of local monitoring stations in Santa Clara County.
- Image gen: Generates campaign hero banners and before/after restorative visions (e.g., "AI visualization of Coyote Creek restored riparian zone and permeable bioswales").
- Sandbox: Computes impact projections (e.g. calculating acre-feet of groundwater recharged based on community bioswale square footage and rainfall data).

Recommended for every project: memory, storage, tools, image generation, A2UI
Agent-specific / stretch: Google Maps JavaScript API embed / dynamic hotspot visualization, Code Sandbox for hydrological impact calculation, Vertex AI Memory Bank for cross-session civic history.
