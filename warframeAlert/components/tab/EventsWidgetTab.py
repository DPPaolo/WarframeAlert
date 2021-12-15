# coding=utf-8
from typing import List, Tuple

from PyQt6 import QtWidgets, QtCore, QtGui

from warframeAlert.components.common.BountyBox import create_bounty_box
from warframeAlert.components.common.ClanEvent import ClanEvent
from warframeAlert.components.common.EmptySpace import EmptySpace
from warframeAlert.components.common.Event import EventType, Event
from warframeAlert.components.common.EventReward import EventReward
from warframeAlert.components.common.EventVaultTrader import EventVaultTrader
from warframeAlert.components.common.HubEvent import create_hub_event
from warframeAlert.components.common.ReconstructionRelayEvent import ReconstructionRelayEvent, get_reconstruction_task
from warframeAlert.components.common.ScoreEvent import ScoreEvent
from warframeAlert.components.common.SpecialAlert import create_alert
from warframeAlert.components.common.Spoiler import Spoiler
from warframeAlert.components.common.SquadLinkEvent import SquadLinkEvent
from warframeAlert.components.widget.AlertWidget import AlertWidget
from warframeAlert.constants.warframeTypes import Goals, ConstructionProjects, Alerts, Goal, PrimeVaultTraders, \
    PrimeVaultTradersData
from warframeAlert.services.notificationService import NotificationService
from warframeAlert.services.optionHandlerService import OptionsHandler
from warframeAlert.services.translationService import translate
from warframeAlert.utils import timeUtils, gameTranslationUtils
from warframeAlert.utils.commonUtils import print_traceback, remove_widget, get_last_item_with_backslash, bool_to_yes_no
from warframeAlert.utils.gameTranslationUtils import get_node, get_region, get_syndicate, get_faction, \
    get_item_name_en, get_item_name, get_vip_agent, get_node_it
from warframeAlert.utils.logUtils import LogHandler
from warframeAlert.utils.warframeUtils import parse_reward


class EventsWidgetTab():

    def __init__(self) -> None:
        self.alerts: dict[str, List[Event | ScoreEvent | ClanEvent | ReconstructionRelayEvent | SquadLinkEvent]] \
            = {'Goals': []}
        self.vault_traders: dict[str, List[EventVaultTrader]] = {'VaultTraders': []}

        self.eventsWidget = QtWidgets.QWidget()

        self.alertWidget = AlertWidget()
        self.eventWidget = QtWidgets.QWidget()
        self.eventRazorWidget = QtWidgets.QWidget()
        self.eventCetusWidget = QtWidgets.QWidget()
        self.eventRelayWidget = QtWidgets.QWidget()
        self.eventSquadLinkWidget = QtWidgets.QWidget()
        self.eventVaultTraderWidget = QtWidgets.QWidget()

        self.eventGrid = QtWidgets.QGridLayout(self.eventsWidget)

        self.AlertScrollBar = QtWidgets.QScrollArea()
        self.EventScrollBarA = QtWidgets.QScrollArea()
        self.EventScrollBarB = QtWidgets.QScrollArea()
        self.EventScrollBarC = QtWidgets.QScrollArea()
        self.EventScrollBarD = QtWidgets.QScrollArea()
        self.EventScrollBarE = QtWidgets.QScrollArea()
        self.EventScrollBarF = QtWidgets.QScrollArea()

        self.AlertScrollBar.setWidgetResizable(True)
        self.EventScrollBarA.setWidgetResizable(True)
        self.EventScrollBarB.setWidgetResizable(True)
        self.EventScrollBarC.setWidgetResizable(True)
        self.EventScrollBarD.setWidgetResizable(True)
        self.EventScrollBarE.setWidgetResizable(True)
        self.EventScrollBarF.setWidgetResizable(True)

        self.AlertScrollBar.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.EventScrollBarA.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.EventScrollBarB.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.EventScrollBarC.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.EventScrollBarD.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.EventScrollBarE.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.EventScrollBarF.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        self.AlertScrollBar.setBackgroundRole(QtGui.QPalette.ColorRole.Light)
        self.EventScrollBarA.setBackgroundRole(QtGui.QPalette.ColorRole.Light)
        self.EventScrollBarB.setBackgroundRole(QtGui.QPalette.ColorRole.Light)
        self.EventScrollBarC.setBackgroundRole(QtGui.QPalette.ColorRole.Light)
        self.EventScrollBarD.setBackgroundRole(QtGui.QPalette.ColorRole.Light)
        self.EventScrollBarE.setBackgroundRole(QtGui.QPalette.ColorRole.Light)
        self.EventScrollBarF.setBackgroundRole(QtGui.QPalette.ColorRole.Light)

        self.EventGrid = QtWidgets.QGridLayout(self.eventWidget)
        self.EventRazorGrid = QtWidgets.QGridLayout(self.eventRazorWidget)
        self.EventCetusGrid = QtWidgets.QGridLayout(self.eventCetusWidget)
        self.EventRelayGrid = QtWidgets.QGridLayout(self.eventRelayWidget)
        self.EventSquadLinkGrid = QtWidgets.QGridLayout(self.eventSquadLinkWidget)
        self.EventVaultTraderGrid = QtWidgets.QGridLayout(self.eventVaultTraderWidget)

        self.EventGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.EventRazorGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.EventCetusGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.EventRelayGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.EventSquadLinkGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.EventVaultTraderGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.AlertScrollBar.setWidget(self.alertWidget.get_widget())
        self.EventScrollBarA.setWidget(self.eventWidget)
        self.EventScrollBarB.setWidget(self.eventRazorWidget)
        self.EventScrollBarC.setWidget(self.eventCetusWidget)
        self.EventScrollBarD.setWidget(self.eventRelayWidget)
        self.EventScrollBarE.setWidget(self.eventSquadLinkWidget)
        self.EventScrollBarF.setWidget(self.eventVaultTraderWidget)

        self.EventTabber = QtWidgets.QTabWidget(self.eventsWidget)

        self.eventGrid.addWidget(self.EventTabber, 0, 0)
        self.eventGrid.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)

        self.eventsWidget.setLayout(self.eventGrid)

    def get_widget(self) -> QtWidgets.QWidget:
        return self.eventsWidget

    def get_length(self) -> int:
        return self.alertWidget.get_length() + len(self.alerts['Goals'])

    def update_alert_mission(self, data: Alerts) -> None:
        if (OptionsHandler.get_option("Tab/TactAll") == 1):
            try:
                self.alertWidget.parse_alert_data(data)
            except Exception as er:
                LogHandler.err(translate("eventsWidget", "alertError") + ": " + str(er))
                print_traceback(translate("eventsWidget", "alertError") + ": " + str(er))
                self.alertWidget.reset_alerts()
        else:
            self.alertWidget.reset_alerts()

    def update_events(self, data: Goals, relay: ConstructionProjects) -> None:
        if (OptionsHandler.get_option("Tab/TactAll") == 1):
            try:
                self.parse_events(data, relay)
            except Exception as er:
                LogHandler.err(translate("eventsWidget", "eventsError") + ": " + str(er))
                print_traceback(translate("eventsWidget", "eventsError") + ": " + str(er))
                self.reset_events()
                return
        else:
            self.reset_events()

    def parse_events(self, data: Goals, relay: ConstructionProjects) -> None:
        self.reset_events()
        if (data):
            n_event = len(self.alerts['Goals'])
            for events in data:
                event_id = events['_id']['$oid']
                found = 0
                for event in self.alerts['Goals']:
                    if (event.get_event_id() == event_id):
                        found = 1

                if (found == 0):
                    temp = create_event(event_id, events, relay)
                    self.alerts['Goals'].append(temp)
                    del temp

            self.add_events(n_event)

    def add_events(self, n_event: int) -> None:
        title = translate("eventsWidget", "newEvent")
        for i in range(n_event, len(self.alerts['Goals'])):
            if (self.alerts['Goals'][i].get_event_type() == EventType.GENERAL):
                self.EventGrid.addLayout(self.alerts['Goals'][i].TAEventBox, self.EventGrid.count(), 0)
            elif (self.alerts['Goals'][i].get_event_type() == EventType.FOMORIAN):
                self.EventRazorGrid.addLayout(self.alerts['Goals'][i].TAEventBox, self.EventRazorGrid.count(), 0)
                if (self.alerts['Goals'][i].get_faction() == "Corpus"):
                    title = translate("eventsWidget", "newRazorbackEvent")
                else:
                    title = translate("eventsWidget", "newFomorianEvent")
            elif (self.alerts['Goals'][i].get_event_type() == EventType.GHOUL):
                self.EventCetusGrid.addLayout(self.alerts['Goals'][i].TAEventBox, self.EventCetusGrid.count(), 0)
                title = translate("eventsWidget", "newCetusEvent")
            elif (self.alerts['Goals'][i].get_event_type() == EventType.RECOSTRUCTION):
                self.EventRelayGrid.addLayout(self.alerts['Goals'][i].TAEventBox, self.EventRelayGrid.count(), 0)
                title = translate("eventsWidget", "newReconstructionEvent")
            elif (self.alerts['Goals'][i].get_event_type() == EventType.SQUAD_LINK):
                self.EventSquadLinkGrid.addLayout(self.alerts['Goals'][i].TAEventBox,
                                                  self.EventSquadLinkGrid.count(), 0)
                title = translate("eventsWidget", "newSquadLinkEvent")

            NotificationService.send_notification(
                title,
                self.alerts['Goals'][i].get_title(),
                self.alerts['Goals'][i].get_image())

    def reset_events(self) -> None:
        cancelled = []
        for i in range(0, len(self.alerts['Goals'])):
            if (self.alerts['Goals'][i].is_expired()):
                cancelled.append(i)
        i = len(cancelled)
        while i > 0:
            self.alerts['Goals'][cancelled[i - 1]].hide()
            remove_widget(self.alerts['Goals'][cancelled[i - 1]].TAEventBox)
            del self.alerts['Goals'][cancelled[i - 1]]
            i -= 1

    def parse_prime_vault_traders(self, data: PrimeVaultTraders) -> None:
        self.reset_prime_vault_traders()
        if (data):
            n_event = len(self.vault_traders['VaultTraders'])
            for trade_event in data:
                event_id = trade_event['_id']['$oid']
                found = 0
                for event in self.vault_traders['VaultTraders']:
                    if (event.get_event_id() == event_id):
                        found = 1
                if (found == 0):
                    temp = create_prime_vault_trader(event_id, trade_event)
                    self.vault_traders['VaultTraders'].append(temp)
                    del temp
            self.add_vault_events(n_event)

    def add_vault_events(self, n_event: int) -> None:
        for i in range(n_event, len(self.vault_traders['VaultTraders'])):

            self.EventVaultTraderGrid.addLayout(self.vault_traders['VaultTraders'][i].TAEventBox,
                                                self.EventVaultTraderGrid.count(), 0)

            NotificationService.send_notification(
                translate("eventsWidget", "newVaultEvent"),
                self.vault_traders['VaultTraders'][i].get_title(),
                None)

    def reset_prime_vault_traders(self) -> None:
        cancelled = []
        for i in range(0, len(self.vault_traders['VaultTraders'])):
            if (self.vault_traders['VaultTraders'][i].is_expired()):
                cancelled.append(i)
        i = len(cancelled)
        while i > 0:
            self.vault_traders['VaultTraders'][cancelled[i - 1]].hide()
            remove_widget(self.vault_traders['VaultTraders'][cancelled[i - 1]].TAEventBox)
            del self.vault_traders['VaultTraders'][cancelled[i - 1]]
            i -= 1

    def update_tab(self) -> None:
        alerts_length = self.alertWidget.get_length()
        events_length = len(self.alerts['Goals'])
        vault_events_length = len(self.vault_traders['VaultTraders'])
        self.EventTabber.insertTab(0, self.AlertScrollBar, translate("eventsWidget", "alerts"))
        if (not (alerts_length > 0)):
            self.EventTabber.removeTab(self.EventTabber.indexOf(self.AlertScrollBar))

        if (events_length > 0):
            self.EventTabber.insertTab(1, self.EventScrollBarA, translate("eventsWidget", "genericEvent"))
            self.EventTabber.insertTab(2, self.EventScrollBarB, translate("eventsWidget", "fomorian"))
            self.EventTabber.insertTab(3, self.EventScrollBarC, translate("eventsWidget", "ghoul"))
            self.EventTabber.insertTab(4, self.EventScrollBarD, translate("eventsWidget", "reconstruction"))
            self.EventTabber.insertTab(5, self.EventScrollBarE, translate("eventsWidget", "squadLink"))

            n_events = n_fomorian = n_cetus = n_relay = n_squad_link = 0
            for i in range(0, events_length):
                if (self.alerts['Goals'][i].get_event_type() == EventType.GENERAL):
                    n_events += 1
                elif (self.alerts['Goals'][i].get_event_type() == EventType.FOMORIAN):
                    n_fomorian += 1
                elif (self.alerts['Goals'][i].get_event_type() == EventType.GHOUL):
                    n_cetus += 1
                elif (self.alerts['Goals'][i].get_event_type() == EventType.RECOSTRUCTION):
                    n_relay += 1
                elif (self.alerts['Goals'][i].get_event_type() == EventType.SQUAD_LINK):
                    n_squad_link += 1
            if (not (n_events > 0)):
                self.EventTabber.removeTab(self.EventTabber.indexOf(self.EventScrollBarA))
            if (not (n_fomorian > 0)):
                self.EventTabber.removeTab(self.EventTabber.indexOf(self.EventScrollBarB))
            if (not (n_cetus > 0)):
                self.EventTabber.removeTab(self.EventTabber.indexOf(self.EventScrollBarC))
            if (not (n_relay > 0)):
                self.EventTabber.removeTab(self.EventTabber.indexOf(self.EventScrollBarD))
            if (not (n_squad_link > 0)):
                self.EventTabber.removeTab(self.EventTabber.indexOf(self.EventScrollBarE))

        self.EventTabber.insertTab(6, self.EventScrollBarF, translate("eventsWidget", "vaultTrader"))
        if (not (vault_events_length > 0)):
            self.EventTabber.removeTab(self.EventTabber.indexOf(self.EventScrollBarF))


def create_event(event_id: str, event: Goal, relay: ConstructionProjects) \
        -> Event | ScoreEvent | ClanEvent | ReconstructionRelayEvent | SquadLinkEvent:
    icon = tooltip = success = regions = faction = ""
    req_item = roaming_vip = mission_map_rotation = ""
    personal = clamp_score = emblem = "No"
    mission_interval = 0
    stratos_present = False
    req_mis: List[str] = []
    init = timeUtils.get_time(event['Activation']['$date']['$numberLong'])
    end = event['Expiry']['$date']['$numberLong']
    if ('Personal' in event):
        personal = bool_to_yes_no(event['Personal'])
    if ('Count' in event):
        count = event['Count']
    else:
        count = 0
    name = event['Tag']
    desc = gameTranslationUtils.get_item_name_en(event['Desc'])
    if ('ToolTip' in event):
        tooltip = get_last_item_with_backslash(event['ToolTip'])
    if ('ScoreLocTag' in event):
        tooltip = tooltip or get_last_item_with_backslash(event['ScoreLocTag'])
    if ('MissionKeyName' in event):
        tooltip = tooltip or get_last_item_with_backslash(event['MissionKeyName'])
    if ('ConcurrentMissionKeyNames' in event):
        tooltip = tooltip or get_last_item_with_backslash(event['ConcurrentMissionKeyNames'][-1])
    if ('ScoreVar' in event):
        tooltip = tooltip or event['ScoreVar']
    if ('ScoreMaxTag' in event):
        tooltip = tooltip or event['ScoreMaxTag']
    if ('Icon' in event):
        icon = event['Icon']
    if ('MissionKeyRotationInterval' in event):
        mission_interval = event['MissionKeyRotationInterval']
    if ('MissionKeyRotation' in event):
        for index, rotation in enumerate(event['MissionKeyRotation']):
            mission_map_rotation += rotation
            if (index < (len(event['MissionKeyRotation']) - 1)):
                mission_map_rotation += "\n"

    community = bool_to_yes_no(event['Community'] if ('Community' in event) else False)
    if ('ClampNodeScores' in event):
        clamp_score = bool_to_yes_no(event['ClampNodeScores'])
    if ('Bounty' in event):
        stratos_present = event['Bounty']
        emblem = bool_to_yes_no(event['Bounty'])
    if ('Success' in event):
        success = bool_to_yes_no(event['Success'])
    if ('Regions' in event):
        for index, region in enumerate(event['Regions']):
            regions += get_region(region)
            if (index < (len(event['Regions']) - 1)):
                regions += ", "
    if ('RegionIdx' in event):
        if (regions != ""):
            regions += ", "
        regions += get_region(event['RegionIdx'])
    if ('Faction' in event):
        faction = get_faction(event['Faction'])
    if ('InstructionalItem' in event):
        req_item = get_item_name_en(event['InstructionalItem'])
    if ('RoamingVIP' in event):
        roaming_vip = get_vip_agent(event['RoamingVIP'])
    if ('PrereqGoalTags' in event):
        req_mis = event['PrereqGoalTags']

    # Fomorian, Razorback or Ghoul Data
    health = fomorian = 0
    att_node = ["", ""]
    best = score = transmission = optional_in_mission = upgrade_ids = ""
    region_drop = archwing_drop = score_block_guilds = ""

    if ('Fomorian' in event):
        fomorian = event['Fomorian']
    if ('HealthPct' in event):
        health = event['HealthPct']
    if ('VictimNode' in event):
        att_node = get_node(event['VictimNode'])
    if ('Transmission' in event):
        transmission = event['Transmission']
    if ('OptionalInMission' in event):
        optional_in_mission = bool_to_yes_no(event['OptionalInMission'])
    if ('UpgradeIds' in event):
        for upgrade in event['UpgradeIds']:
            upgrade_ids += upgrade['$oid'] + ","
        upgrade_ids = upgrade_ids[:-1]
    if ('RegionDrops' in event):
        for i in range(0, len(event['RegionDrops'])):
            region_drop += get_item_name(event['RegionDrops'][i])
            if (i < len(event['RegionDrops'])):
                region_drop += "\n"
    if ('ArchwingDrops' in event):
        for i in range(0, len(event['ArchwingDrops'])):
            archwing_drop += get_item_name(event['ArchwingDrops'][i])
            if (i < len(event['ArchwingDrops'])):
                archwing_drop += "\n"
    if ('Best' in event):
        best = bool_to_yes_no(event['Best'])
    if ('ScoreTagBlocksGuildTierChanges' in event):
        score_block_guilds = bool_to_yes_no(event['Best'])

    # Clan Event Data
    req_node: Tuple[str, str] = ("", "")
    clan_goal: List[str] = []
    if ('ClanGoal' in event):
        clan_goal = event['ClanGoal']
    if ('RewardNode' in event):
        req_node = get_node(event['RewardNode'])

    # Relay Reconstruction Data
    relay_reconstruction = 0
    relay_node = ""
    if ('RelayReconstruction' in event):
        relay_reconstruction = event['RelayReconstruction']
        relay_node = event['Node']

    # Squad Link Data
    alt_activation = alt_expiry = next_alt_activation = next_alt_expiry = 0
    completion_bonus = epoch_number = pause_scheduling = metadata = ""
    if ('AltActivation' in event):
        alt_activation = event['AltActivation']['$date']['$numberLong']
    if ('AltExpiry' in event):
        alt_expiry = event['AltExpiry']['$date']['$numberLong']
    if ('NextAltActivation' in event):
        next_alt_activation = event['NextAltActivation']['$date']['$numberLong']
    if ('NextAltExpiry' in event):
        next_alt_expiry = event['NextAltExpiry']['$date']['$numberLong']
    if ('CompletionBonus' in event):
        completion_bonus = event['CompletionBonus']
    if ('EpochNum' in event):
        epoch_number = event['EpochNum']
    if ('PauseAutoScheduling' in event):
        pause_scheduling = bool_to_yes_no(event['PauseAutoScheduling'])
    if ('Metadata' in event):
        metadata = event['Metadata']

    if (health):
        temp = ScoreEvent(event_id)
        temp.set_perc_att(health, att_node)
        temp.set_score_data(score, best)
        temp.set_score_optional_tooltip(optional_in_mission, upgrade_ids, score_block_guilds)
        if (fomorian):
            temp.set_event_type(EventType.FOMORIAN)
        elif ('Jobs' in event):
            temp.set_event_type(EventType.GHOUL)
        else:
            temp.set_event_type(EventType.GENERAL)
    elif (len(clan_goal) != 0):
        temp = ClanEvent(event_id, req_node)
        temp.set_clan_score(clan_goal)
    elif (relay_reconstruction):
        task = get_reconstruction_task(name, relay)
        temp = ReconstructionRelayEvent(event_id)
        temp.add_relay_reconstruction(regions, relay_node, task)
        temp.set_event_type(EventType.RECOSTRUCTION)
    elif (alt_activation and alt_expiry):
        temp = SquadLinkEvent(event_id)
        temp.set_squad_link_data(alt_activation, alt_expiry, next_alt_activation, next_alt_expiry)
        temp.set_squad_link_extra_data(completion_bonus, epoch_number, pause_scheduling, metadata)
        temp.set_event_type(EventType.SQUAD_LINK)
    else:
        temp = Event(event_id)

    temp.set_event_name(name, desc, tooltip, icon, stratos_present)
    temp.set_event_info(init, end, count, personal, clamp_score, emblem, transmission, community)
    temp.set_optional_field(regions, success, faction, req_item, roaming_vip, req_mis)

    # Hub Event Data
    if ('ContinuousHubEvent' in event):
        hub = event['ContinuousHubEvent']
        hub = create_hub_event(hub)
        if (archwing_drop != ""):
            tag_h = translate("eventsWidget", "razorbackHubEvent")
        elif (region_drop != ""):
            tag_h = translate("eventsWidget", "fomorianHubEvent")
        else:
            tag_h = translate("eventsWidget", "hubEvent")
        hub.set_hub_name(tag_h)

        temp.add_event_object(EmptySpace().SpaceBox)
        temp.add_event_object(hub.HubBox)

    # Bounty Data
    if ('PreviousJobs' in event):
        for job in event['PreviousJobs']:
            bounty = create_bounty_box(job)
            if ('JobAffiliationTag' in event):
                syn = get_syndicate(event['JobAffiliationTag'])
                bounty.set_syndicate(syn, translate("eventsWidget", "event"), False)
            if ('JobPreviousVersion' in event):
                bounty.set_bounty_id(event['JobPreviousVersion']['$oid'])

            spoiler = Spoiler(translate("eventsWidget", "oldBounty"))
            spoiler.set_content_layout(bounty.BountyBox)
            temp.add_event_widget(spoiler)

    if ('Jobs' in event):
        for job in event['Jobs']:
            bounty = create_bounty_box(job)
            if ('JobAffiliationTag' in event):
                syn = get_syndicate(event['JobAffiliationTag'])
                bounty.set_syndicate(syn, translate("eventsWidget", "event"), False)
            if ('JobCurrentVersion' in event):
                bounty.set_bounty_id(event['JobCurrentVersion']['$oid'])

            temp.add_event_object(EmptySpace().SpaceBox)
            temp.add_event_object(bounty.BountyBox)

    # Mission Data
    if ('MissionInfo' in event):
        alert = create_alert(event['MissionInfo'], str(timeUtils.get_local_time()))
        if (alert is not None):
            temp.add_event_object(EmptySpace().SpaceBox)
            temp.add_event_object(alert.AlertBox)

    # Rewards Data
    goal = []
    node = []
    rew = []
    req = [0]

    if ('InterimGoals' in event):
        for temp_goal in event['InterimGoals']:
            goal.append(temp_goal)
    if ('Goal' in event):
        goal.append(event['Goal'])
    if ('BonusGoal' in event):
        goal.append(event['Goal'])

    if ('InterimRewards' in event):
        for tempReward in event['InterimRewards']:
            rew.append(parse_reward(tempReward))
    if ('Reward' in event):
        rew.append(parse_reward(event['Reward']))
    if ('BonusReward' in event):
        rew.append(parse_reward(event['Reward']))

    if ('ConcurrentNodeReqs' in event):
        for temp_req in event['ConcurrentNodeReqs']:
            req.append(temp_req)

    if ('Node' in event):
        node.append(get_node(event['Node']))
    if ('ConcurrentNodes' in event):
        for temp_node in event['ConcurrentNodes']:
            node.append(get_node(temp_node))
    g_len = len(goal)
    n_len = len(node)
    r_len = len(rew)
    req_len = len(req)

    temp.add_event_object(EmptySpace().SpaceBox)

    if (g_len == r_len):
        if (g_len != n_len):
            for i in range(n_len, g_len):
                node.append(node[0])
        if (g_len != req_len):
            for i in range(req_len, g_len):
                req.append(req[0])
        for i in range(0, g_len):
            event_rew = EventReward(i + 1)
            event_rew.set_reward_data(rew[i], node[i], goal[i], req[i], mission_interval, mission_map_rotation)
            temp.add_event_object(event_rew.TAVBox)
            temp.add_event_object(EmptySpace().SpaceBox)

    # LogHandler.debug("Evento: " + name)
    # LogHandler.debug("Numero Goal: " + str(g_len))
    # LogHandler.debug("Numero Nodi: " + str(n_len))
    # LogHandler.debug("Numero Ricompense: " + str(r_len))
    # LogHandler.debug("Numero Requisiti: " + str(req_len))

    return temp


def create_prime_vault_trader(event_id: str, event: PrimeVaultTradersData) -> EventVaultTrader:
    init = timeUtils.get_time(event['Activation']['$date']['$numberLong'])
    end = event['Expiry']['$date']['$numberLong']
    initial_init = timeUtils.get_time(event['InitialStartDate']['$date']['$numberLong'])
    completed = bool_to_yes_no(event['Completed'])
    node = get_node_it(event['Node'])
    params = event['Params'] if ('Params' in event) else ""
    phase = event['Phase'] if ('Phase' in event) else 0
    manifest = event['Manifest']
    schedule_info = event['ScheduleInfo']

    temp = EventVaultTrader(event_id)
    temp.set_event_info(init, end, initial_init, completed, node[0], params, phase)
    temp.set_manifest_data(manifest)
    temp.set_schedule_data(schedule_info)

    return temp
