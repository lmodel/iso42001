from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "2023"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'annotations': {'edition': {'tag': 'edition', 'value': '1'},
                     'iso_open_data_date': {'tag': 'iso_open_data_date',
                                            'value': '2026-11-05'},
                     'normative_reference': {'tag': 'normative_reference',
                                             'value': 'ISO/IEC 22989:2022'},
                     'publication_date': {'tag': 'publication_date',
                                          'value': '2023-12-18'},
                     'standard': {'tag': 'standard',
                                  'value': 'ISO/IEC 42001:2023'}},
     'comments': ['The version is the edition the schema models, and source is '
                  "ISO's page for it. ISO Open Data's records of the edition and "
                  'of its normative reference are copied to '
                  'src/iso42001/schema/iso-open-data/ on the date the annotations '
                  'give, and scripts/check_upstream_release.py reports when ISO '
                  "changes them. The release tags are the schema's own versions.",
                  'ISO/IEC 42001 is copyright ISO and IEC, and none of its text is '
                  'reproduced here. An element cites what it models by number, in '
                  'the iso42001_clause, annex_a_control, annex_b_item, '
                  'annex_c_item or annex_d_item annotation, and its title and '
                  "description are this project's own words. A reader with a "
                  "licensed copy looks the text up by that number, and a record's "
                  "title and description hold the organization's own words.",
                  'The terms follow ISO/IEC 22989:2022, the one normative '
                  "reference, and so do the stages of a system's life and the "
                  'kinds of AI role. Annexes C and D are informative and give '
                  'examples, so an enum built from one of them has the value '
                  'other.',
                  'Every record that other records refer to has an aims_id, and a '
                  'reference holds that identifier. AimsManagementSystem holds '
                  'each kind of record in a list of its own.',
                  'A close mapping to lmodel/iso27001 names the class that answers '
                  'to the same clause number, since both standards follow the '
                  'harmonized structure of management system standards. '
                  'AimsOrganization and AimsRole are the same kind of thing as '
                  "SPDX's Organization and OSCAL's Role. AimsControl is related to "
                  "OSCAL's Control: both name a safeguard, but OSCAL's is a "
                  "catalogue entry and this one is the organization's own.",
                  'An AI system and an impact it has are the same kind of thing as '
                  'the AI system and the impact of lmodel/nist-ai-100-1, and a '
                  'risk is related to its risk, as that schema relates its risk to '
                  "lmodel/iso27001's. The parts a party plays with personal data "
                  'map to the controller and the processor of lmodel/iso29100, '
                  'which models the standard AimsPiiRole names.'],
     'default_prefix': 'iso42001',
     'default_range': 'string',
     'description': 'A LinkML model of the records an organization keeps to run an '
                    'artificial intelligence (AI) management system under ISO/IEC '
                    '42001:2023. The records cover its context, leadership, '
                    'planning and support, how it weighs and treats AI risks, and '
                    'what its AI systems may do to people and society. They also '
                    'cover those systems with their resources, data and documents, '
                    'its audits and reviews, and what it corrects and improves. '
                    'The reference controls of Annex A appear by number, with '
                    "titles of this project's own.",
     'id': 'https://w3id.org/lmodel/iso42001',
     'imports': ['linkml:types'],
     'license': 'Apache-2.0',
     'name': 'iso42001',
     'prefixes': {'iso27001': {'prefix_prefix': 'iso27001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso27001/'},
                  'iso29100': {'prefix_prefix': 'iso29100',
                               'prefix_reference': 'https://w3id.org/lmodel/iso29100/'},
                  'iso42001': {'prefix_prefix': 'iso42001',
                               'prefix_reference': 'https://w3id.org/lmodel/iso42001/'},
                  'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_ai_100_1': {'prefix_prefix': 'nist_ai_100_1',
                                    'prefix_reference': 'https://w3id.org/lmodel/nist-ai-100-1/'},
                  'oscal': {'prefix_prefix': 'oscal',
                            'prefix_reference': 'https://w3id.org/lmodel/oscal/'},
                  'schema': {'prefix_prefix': 'schema',
                             'prefix_reference': 'http://schema.org/'},
                  'spdx_core': {'prefix_prefix': 'spdx_core',
                                'prefix_reference': 'https://spdx.org/rdf/3.0.1/terms/Core/'},
                  'xsd': {'prefix_prefix': 'xsd',
                          'prefix_reference': 'http://www.w3.org/2001/XMLSchema#'}},
     'see_also': ['https://lmodel.github.io/iso42001',
                  'https://www.iso.org/standard/81230.html',
                  'https://www.iso.org/standard/74296.html'],
     'source': 'https://www.iso.org/standard/81230.html',
     'source_file': 'src/iso42001/schema/iso42001.yaml',
     'subsets': {'aims_ai_system_records': {'description': 'The AI systems, their '
                                                           'resources, data and '
                                                           'documents, and what is '
                                                           'told to those who use '
                                                           'or depend on them '
                                                           '(Annex A, areas A.4 '
                                                           'and A.6 to A.9).',
                                            'from_schema': 'https://w3id.org/lmodel/iso42001',
                                            'name': 'aims_ai_system_records'},
                 'aims_annex_a': {'description': 'The Annex A reference controls, '
                                                 "the organization's own controls "
                                                 'and the Statement of '
                                                 'Applicability.',
                                  'from_schema': 'https://w3id.org/lmodel/iso42001',
                                  'name': 'aims_annex_a'},
                 'aims_core': {'description': "The records of the system's "
                                              'context, leadership, planning and '
                                              'support (clauses 4 to 7).',
                               'from_schema': 'https://w3id.org/lmodel/iso42001',
                               'name': 'aims_core'},
                 'aims_documented_information': {'description': 'The records that '
                                                                'are documented '
                                                                'information under '
                                                                'document control '
                                                                '(clause 7.5).',
                                                 'from_schema': 'https://w3id.org/lmodel/iso42001',
                                                 'name': 'aims_documented_information'},
                 'aims_external_parties': {'description': 'The relationships with '
                                                          'partners, suppliers and '
                                                          'customers (Annex A, '
                                                          'area A.10).',
                                           'from_schema': 'https://w3id.org/lmodel/iso42001',
                                           'name': 'aims_external_parties'},
                 'aims_improvement': {'description': 'The records of getting '
                                                     'better: improvements, '
                                                     'nonconformities and what '
                                                     'corrects them (clause 10).',
                                      'from_schema': 'https://w3id.org/lmodel/iso42001',
                                      'name': 'aims_improvement'},
                 'aims_performance_evaluation': {'description': 'The records of '
                                                                'monitoring, '
                                                                'internal audit '
                                                                'and management '
                                                                'review (clause '
                                                                '9).',
                                                 'from_schema': 'https://w3id.org/lmodel/iso42001',
                                                 'name': 'aims_performance_evaluation'},
                 'aims_risk_management': {'description': 'The records of risk '
                                                         'assessment, risk '
                                                         'treatment and impact '
                                                         'assessment (clauses 6.1, '
                                                         '8.2, 8.3 and 8.4).',
                                          'from_schema': 'https://w3id.org/lmodel/iso42001',
                                          'name': 'aims_risk_management'}},
     'title': 'ISO/IEC 42001:2023 AI management system records',
     'types': {'aims_duration': {'base': 'str',
                                 'comments': ['The pattern is that of '
                                              'xsd:duration, which has no weeks, '
                                              'so two weeks is P14D.'],
                                 'description': 'A length of time as ISO 8601 '
                                                'writes it, such as P7Y for seven '
                                                'years or P30D for thirty days.',
                                 'from_schema': 'https://w3id.org/lmodel/iso42001',
                                 'name': 'aims_duration',
                                 'pattern': '^P(?=[0-9T])([0-9]+Y)?([0-9]+M)?([0-9]+D)?(T(?=[0-9])([0-9]+H)?([0-9]+M)?([0-9]+S)?)?$',
                                 'typeof': 'string',
                                 'uri': 'xsd:duration'}}} )

class AimsClause(str, Enum):
    """
    The numbered clauses and subclauses of the standard from 4 to 10, by their numbers. A value's description is this project's own summary, and the clause headings and the requirements are ISO's.
    """
    number_4 = "clause_4"
    """
    Why the system exists and what it reaches.
    """
    number_4FULL_STOP1 = "clause_4_1"
    """
    Matters inside and outside that bear on the system, climate among them, and the part the organization plays with AI.
    """
    number_4FULL_STOP2 = "clause_4_2"
    """
    Who has a stake in the system, and what they want from it.
    """
    number_4FULL_STOP3 = "clause_4_3"
    """
    Where the system stops, stated in writing.
    """
    number_4FULL_STOP4 = "clause_4_4"
    """
    Having the system and its processes in place, and keeping them up.
    """
    number_5 = "clause_5"
    """
    What top management must do.
    """
    number_5FULL_STOP1 = "clause_5_1"
    """
    How top management shows it leads and backs the system.
    """
    number_5FULL_STOP2 = "clause_5_2"
    """
    Management's written direction on AI.
    """
    number_5FULL_STOP3 = "clause_5_3"
    """
    Who holds which duty and power, including who checks conformity and who reports on performance.
    """
    number_6 = "clause_6"
    """
    Deciding what to do before doing it.
    """
    number_6FULL_STOP1 = "clause_6_1"
    """
    Dealing with what could go well or badly.
    """
    number_6FULL_STOP1FULL_STOP1 = "clause_6_1_1"
    """
    Criteria for risk, and the actions planned on risks and opportunities.
    """
    number_6FULL_STOP1FULL_STOP2 = "clause_6_1_2"
    """
    A repeatable way to find, analyse and rank AI risks.
    """
    number_6FULL_STOP1FULL_STOP3 = "clause_6_1_3"
    """
    Choosing treatments and controls, with the Statement of Applicability and the plan.
    """
    number_6FULL_STOP1FULL_STOP4 = "clause_6_1_4"
    """
    A way to work out what AI systems may do to people and society.
    """
    number_6FULL_STOP2 = "clause_6_2"
    """
    Measurable aims for AI, and how each will be reached.
    """
    number_6FULL_STOP3 = "clause_6_3"
    """
    Changing the system in an orderly way.
    """
    number_7 = "clause_7"
    """
    What the system needs in order to run.
    """
    number_7FULL_STOP1 = "clause_7_1"
    """
    Providing what the system needs.
    """
    number_7FULL_STOP2 = "clause_7_2"
    """
    People's ability to do the work, and the evidence of it.
    """
    number_7FULL_STOP3 = "clause_7_3"
    """
    What those who work for the organization must know.
    """
    number_7FULL_STOP4 = "clause_7_4"
    """
    Who is told what, when and how.
    """
    number_7FULL_STOP5 = "clause_7_5"
    """
    Keeping information under control.
    """
    number_7FULL_STOP5FULL_STOP1 = "clause_7_5_1"
    """
    Which information the system holds.
    """
    number_7FULL_STOP5FULL_STOP2 = "clause_7_5_2"
    """
    Naming, formatting, reviewing and approving it.
    """
    number_7FULL_STOP5FULL_STOP3 = "clause_7_5_3"
    """
    Keeping it to hand and protected.
    """
    number_8 = "clause_8"
    """
    Carrying out what was planned.
    """
    number_8FULL_STOP1 = "clause_8_1"
    """
    Running and controlling the processes, including those from outside.
    """
    number_8FULL_STOP2 = "clause_8_2"
    """
    Carrying out risk assessments, on schedule and when things change.
    """
    number_8FULL_STOP3 = "clause_8_3"
    """
    Carrying out the treatment plan and checking that it works.
    """
    number_8FULL_STOP4 = "clause_8_4"
    """
    Carrying out impact assessments, on schedule and when things change.
    """
    number_9 = "clause_9"
    """
    Checking how the system is doing.
    """
    number_9FULL_STOP1 = "clause_9_1"
    """
    What is measured, how and when, and what the results mean.
    """
    number_9FULL_STOP2 = "clause_9_2"
    """
    Audits the organization runs on itself.
    """
    number_9FULL_STOP2FULL_STOP1 = "clause_9_2_1"
    """
    What such an audit must establish, and how often.
    """
    number_9FULL_STOP2FULL_STOP2 = "clause_9_2_2"
    """
    The plan for those audits, and how impartial they are.
    """
    number_9FULL_STOP3 = "clause_9_3"
    """
    Top management's own look at the system.
    """
    number_9FULL_STOP3FULL_STOP1 = "clause_9_3_1"
    """
    How often it looks, and to what end.
    """
    number_9FULL_STOP3FULL_STOP2 = "clause_9_3_2"
    """
    What it must take in.
    """
    number_9FULL_STOP3FULL_STOP3 = "clause_9_3_3"
    """
    What it must produce.
    """
    number_10 = "clause_10"
    """
    Getting better and putting things right.
    """
    number_10FULL_STOP1 = "clause_10_1"
    """
    Making the system better over time.
    """
    number_10FULL_STOP2 = "clause_10_2"
    """
    Dealing with an unmet requirement and removing its cause.
    """


class AimsControlArea(str, Enum):
    """
    The nine areas Annex A sorts its controls into, under names of this project's own. An area's number is its annotation.
    """
    AFULL_STOP2 = "policy_direction"
    """
    Written direction from management on AI, and how it fits with other policies.
    """
    AFULL_STOP3 = "accountability"
    """
    Who answers for AI within the organization's walls, and the way worries are raised.
    """
    AFULL_STOP4 = "system_resources"
    """
    What each AI system draws on: components, data, tools, computing and people.
    """
    AFULL_STOP5 = "impact_assessment"
    """
    Working out what AI systems may do to people and society.
    """
    AFULL_STOP6 = "system_life_cycle"
    """
    Building and running AI systems, from the goals set for them to their logs.
    """
    AFULL_STOP7 = "data_management"
    """
    The data AI systems use: how it is managed, obtained, kept fit, traced and readied.
    """
    AFULL_STOP8 = "stakeholder_information"
    """
    What users and others are told about a system, and their way to report harm.
    """
    AFULL_STOP9 = "responsible_use"
    """
    How AI systems are put to use, against the organization's goals and the systems' documents.
    """
    AFULL_STOP10 = "external_relationships"
    """
    Duties shared with partners, suppliers and customers.
    """


class AimsAnnexAControl(str, Enum):
    """
    The 38 reference controls of Annex A, by number. A value's title holds the number and a name of this project's own, and its description says in this project's words what the control asks for.
    """
    AFULL_STOP2FULL_STOP2_Written_direction_on_AI = "a_2_2"
    """
    Set down in writing how the organization means to treat AI systems.
    """
    AFULL_STOP2FULL_STOP3_Fit_with_other_policies = "a_2_3"
    """
    Find where the organization's other policies touch its aims for AI, in either direction.
    """
    AFULL_STOP2FULL_STOP4_Regular_policy_check = "a_2_4"
    """
    Look at the AI policy again on a schedule and whenever the need arises, to see that it still serves.
    """
    AFULL_STOP3FULL_STOP2_Who_answers_for_what = "a_3_2"
    """
    Decide who carries which duty for AI, as the organization's needs dictate.
    """
    AFULL_STOP3FULL_STOP3_A_way_to_raise_worries = "a_3_3"
    """
    Give people a way to raise worries about the organization's part in a system, at any point in that system's life.
    """
    AFULL_STOP4FULL_STOP2_Inventory_of_what_is_needed = "a_4_2"
    """
    List what each stage of a system's life, and other AI work, draws on.
    """
    AFULL_STOP4FULL_STOP3_Record_of_data_used = "a_4_3"
    """
    Record facts about the data a system draws on.
    """
    AFULL_STOP4FULL_STOP4_Record_of_tools_used = "a_4_4"
    """
    Record facts about the tools a system draws on.
    """
    AFULL_STOP4FULL_STOP5_Record_of_infrastructure_used = "a_4_5"
    """
    Record facts about the hardware and computing a system draws on.
    """
    AFULL_STOP4FULL_STOP6_Record_of_the_people_involved = "a_4_6"
    """
    Record who works on a system across its whole life, and what skills they bring.
    """
    AFULL_STOP5FULL_STOP2_Method_for_weighing_consequences = "a_5_2"
    """
    Set up a way to work out what a system could do to people and society over its life.
    """
    AFULL_STOP5FULL_STOP3_Keeping_assessment_results = "a_5_3"
    """
    Write down what each impact assessment found, and hold on to it for a set time.
    """
    AFULL_STOP5FULL_STOP4_Effects_on_people = "a_5_4"
    """
    Work out and record how a system could affect single persons or particular groups over its life.
    """
    AFULL_STOP5FULL_STOP5_Effects_on_society = "a_5_5"
    """
    Work out and record how a system could affect society over its life.
    """
    AFULL_STOP6FULL_STOP1FULL_STOP2_Goals_for_building = "a_6_1_2"
    """
    Set goals that steer responsible building, and work measures for them into the development cycle.
    """
    AFULL_STOP6FULL_STOP1FULL_STOP3_Defined_ways_of_building = "a_6_1_3"
    """
    Set down the particular processes for designing and building a system responsibly.
    """
    AFULL_STOP6FULL_STOP2FULL_STOP2_What_a_system_must_do = "a_6_2_2"
    """
    Write down what a new system, or a large upgrade to one, must meet.
    """
    AFULL_STOP6FULL_STOP2FULL_STOP3_Build_records = "a_6_2_3"
    """
    Write down how a system was designed and built, against the goals and the requirements.
    """
    AFULL_STOP6FULL_STOP2FULL_STOP4_Checks_and_their_criteria = "a_6_2_4"
    """
    Set the checks that verify and validate a system, and say when each applies.
    """
    AFULL_STOP6FULL_STOP2FULL_STOP5_Going_live = "a_6_2_5"
    """
    Keep a plan for putting a system into service, and meet its conditions first.
    """
    AFULL_STOP6FULL_STOP2FULL_STOP6_Running_and_watching = "a_6_2_6"
    """
    Set down what keeping a system in service takes: at least watching it, fixing it, updating it and supporting it.
    """
    AFULL_STOP6FULL_STOP2FULL_STOP7_Documents_per_audience = "a_6_2_7"
    """
    Decide what technical documents each kind of reader needs, and give them those documents in a suitable form.
    """
    AFULL_STOP6FULL_STOP2FULL_STOP8_Keeping_logs = "a_6_2_8"
    """
    Decide at which points in a system's life it keeps event logs, and keep them at least while it is in service.
    """
    AFULL_STOP7FULL_STOP2_Managing_data_for_building = "a_7_2"
    """
    Set down and follow processes that manage the data used to build systems.
    """
    AFULL_STOP7FULL_STOP3_Obtaining_and_choosing_data = "a_7_3"
    """
    Record how the data a system uses was obtained and picked.
    """
    AFULL_STOP7FULL_STOP4_Data_fit_for_purpose = "a_7_4"
    """
    State what quality data must have, and see that the data used to build and run a system has it.
    """
    AFULL_STOP7FULL_STOP5_Tracing_where_data_came_from = "a_7_5"
    """
    Keep a process that records where data came from and what happened to it, while it and the system last.
    """
    AFULL_STOP7FULL_STOP6_Readying_data = "a_7_6"
    """
    Set criteria for choosing how data is made ready, and name the methods to use.
    """
    AFULL_STOP8FULL_STOP2_What_users_are_told = "a_8_2"
    """
    Work out what those who use a system need to know, and tell them.
    """
    AFULL_STOP8FULL_STOP3_Letting_outsiders_report_harm = "a_8_3"
    """
    Give people outside the organization a way to report harm a system has done.
    """
    AFULL_STOP8FULL_STOP4_Telling_users_about_incidents = "a_8_4"
    """
    Keep a plan for telling those who use a system when something goes wrong.
    """
    AFULL_STOP8FULL_STOP5_Duties_to_inform_others = "a_8_5"
    """
    Work out what the organization owes others by way of reports about a system.
    """
    AFULL_STOP9FULL_STOP2_Defined_ways_of_using = "a_9_2"
    """
    Set down the processes for using AI systems responsibly.
    """
    AFULL_STOP9FULL_STOP3_Goals_for_use = "a_9_3"
    """
    Set goals that steer how AI systems are used responsibly.
    """
    AFULL_STOP9FULL_STOP4_Staying_within_documented_use = "a_9_4"
    """
    See that a system is used only as intended and as its documents say.
    """
    AFULL_STOP10FULL_STOP2_Sharing_out_duties = "a_10_2"
    """
    Settle who carries which duty across a system's life, among the organization and those it deals with.
    """
    AFULL_STOP10FULL_STOP3_What_is_bought_in = "a_10_3"
    """
    Keep a process that holds what suppliers provide to how the organization means to treat AI.
    """
    AFULL_STOP10FULL_STOP4_BuyersAPOSTROPHE_needs = "a_10_4"
    """
    See that how the organization treats AI takes account of what its customers expect and want.
    """


class AimsLifecycleStage(str, Enum):
    """
    The eight stages of the generic life cycle model that ISO/IEC 22989:2022 gives, which ISO/IEC 42001 points to.
    """
    inception = "inception"
    """
    Someone sees a need, weighs whether to meet it, and sets goals.
    """
    design_and_development = "design_and_development"
    """
    The system is designed and built.
    """
    verification_and_validation = "verification_and_validation"
    """
    The system is checked against what was asked of it.
    """
    deployment = "deployment"
    """
    The system is put into service.
    """
    operation_and_monitoring = "operation_and_monitoring"
    """
    The system runs and is watched.
    """
    continuous_validation = "continuous_validation"
    """
    A system that goes on learning is checked again as it changes.
    """
    re_evaluation = "re_evaluation"
    """
    The system's results are weighed against its goals afresh.
    """
    retirement = "retirement"
    """
    The system is taken out of service.
    """


class AimsAiRole(str, Enum):
    """
    The parts an organization or a person can play towards AI systems. The six families are those of ISO/IEC 22989:2022, and each more specific role names its family in an annotation.
    """
    ai_provider = "ai_provider"
    """
    Offers AI systems or platforms to others.
    """
    ai_platform_provider = "ai_platform_provider"
    """
    Offers a platform that others build AI services on.
    """
    ai_product_or_service_provider = "ai_product_or_service_provider"
    """
    Offers goods or services that hold an AI system.
    """
    ai_producer = "ai_producer"
    """
    Makes AI systems.
    """
    ai_developer = "ai_developer"
    """
    Writes and trains what goes into a system.
    """
    ai_designer = "ai_designer"
    """
    Decides how a system should work.
    """
    ai_operator = "ai_operator"
    """
    Keeps a system running.
    """
    ai_tester_or_evaluator = "ai_tester_or_evaluator"
    """
    Checks how well a system does.
    """
    ai_deployer = "ai_deployer"
    """
    Puts a system into service.
    """
    ai_human_factor_professional = "ai_human_factor_professional"
    """
    Looks after how people and a system work together.
    """
    domain_expert = "domain_expert"
    """
    Knows the field a system is used in.
    """
    ai_impact_assessor = "ai_impact_assessor"
    """
    Weighs what a system may do to people and society.
    """
    procurer = "procurer"
    """
    Buys systems or their parts.
    """
    ai_governance_professional = "ai_governance_professional"
    """
    Oversees how AI is run and held to account.
    """
    ai_customer = "ai_customer"
    """
    Takes AI systems from a provider.
    """
    ai_user = "ai_user"
    """
    Works with a system directly.
    """
    ai_partner = "ai_partner"
    """
    Helps others make or run AI systems.
    """
    ai_system_integrator = "ai_system_integrator"
    """
    Joins a system to others.
    """
    data_provider = "data_provider"
    """
    Supplies data for a system.
    """
    ai_subject = "ai_subject"
    """
    Is affected by what a system decides or does.
    """
    data_subject = "data_subject"
    """
    Is someone a system's data is about.
    """
    other_subject = "other_subject"
    """
    Is affected in some other way.
    """
    relevant_authority = "relevant_authority"
    """
    Sets or enforces rules for AI.
    """
    policy_maker = "policy_maker"
    """
    Sets the rules.
    """
    regulator = "regulator"
    """
    Enforces the rules.
    """


class AimsPiiRole(str, Enum):
    """
    The parts a party can play when personal data passes through AI, which ISO/IEC 29100 describes.
    """
    pii_controller = "pii_controller"
    """
    Decides why and how personal data is processed.
    """
    joint_pii_controller = "joint_pii_controller"
    """
    Makes those decisions together with another party.
    """
    pii_processor = "pii_processor"
    """
    Processes personal data on a controller's behalf.
    """


class AimsObjectivePurpose(str, Enum):
    """
    What an AI objective is for. Clause 6.2 asks for objectives in general, and two Annex A controls ask for objectives of a narrower kind.
    """
    organizational = "organizational"
    """
    An objective for the whole system.
    """
    responsible_development = "responsible_development"
    """
    A goal that steers how systems are built.
    """
    responsible_use = "responsible_use"
    """
    A goal that steers how systems are used.
    """


class AimsObjectiveCategory(str, Enum):
    """
    Kinds of objective an organization may set for AI: those Annex C lists, two more from the guidance on responsible use, and other.
    """
    accountability = "accountability"
    """
    Someone stays answerable for what a system helps to do.
    """
    ai_expertise = "ai_expertise"
    """
    The organization has people with the skills AI calls for.
    """
    training_and_test_data = "training_and_test_data"
    """
    Good data to train and check a system is to hand.
    """
    environmental_impact = "environmental_impact"
    """
    A system's effect on the environment is kept in view.
    """
    fairness = "fairness"
    """
    Automated decisions do not wrong particular persons or groups.
    """
    maintainability = "maintainability"
    """
    Defects can be mended and new needs met.
    """
    privacy = "privacy"
    """
    Data about people, sensitive data above all, is neither misused nor exposed.
    """
    robustness = "robustness"
    """
    A system does as well on unseen data as on what it was trained on.
    """
    safety = "safety"
    """
    Nobody's life or health, and no property or part of nature, comes to harm.
    """
    security = "security"
    """
    Threats peculiar to AI are met, beyond the usual ones.
    """
    transparency_and_explainability = "transparency_and_explainability"
    """
    Those concerned can see how a system works and why it gave a result.
    """
    reliability = "reliability"
    """
    A system keeps doing what it is meant to.
    """
    accessibility = "accessibility"
    """
    A system can be used by people with differing abilities.
    """
    other = "other"
    """
    A kind of objective the organization sets for itself.
    """


class AimsRiskSourceCategory(str, Enum):
    """
    Kinds of source a risk from AI can come from: those Annex C lists, and other.
    """
    complex_environment = "complex_environment"
    """
    A system works where situations vary widely, so its results are less sure.
    """
    opaque_system = "opaque_system"
    """
    The organization cannot tell people enough about a system.
    """
    level_of_automation = "level_of_automation"
    """
    How much a system does alone, which bears on safety or fairness among others.
    """
    machine_learning = "machine_learning"
    """
    The data a model learns from, or how it was gathered, is flawed.
    """
    hardware = "hardware"
    """
    Faulty parts, or moving a trained model to other equipment.
    """
    life_cycle = "life_cycle"
    """
    Flaws anywhere in a system's life, from design to retirement.
    """
    technology_readiness = "technology_readiness"
    """
    A technology is too new to know well, or so old it breeds complacency.
    """
    other = "other"
    """
    A source the organization names for itself.
    """


class AimsImpactSubject(str, Enum):
    """
    Who an AI system's impact falls on.
    """
    individuals = "individuals"
    """
    Particular persons.
    """
    groups_of_individuals = "groups_of_individuals"
    """
    Groups of persons, such as children or workers.
    """
    societies = "societies"
    """
    Society at large.
    """


class AimsImpactArea(str, Enum):
    """
    Areas where AI systems can touch people or society: those the guidance on impact assessment names as examples, and other.
    """
    fairness = "fairness"
    """
    Treating persons and groups even-handedly.
    """
    accountability = "accountability"
    """
    Someone staying answerable for the outcome.
    """
    transparency_and_explainability = "transparency_and_explainability"
    """
    Being able to see how a system works and why it gave a result.
    """
    security_and_privacy = "security_and_privacy"
    """
    Keeping people's information safe and private.
    """
    safety_and_health = "safety_and_health"
    """
    Physical and mental harm and wellbeing.
    """
    financial = "financial"
    """
    What people stand to gain or lose in money.
    """
    accessibility = "accessibility"
    """
    Whether people with differing abilities can use a system.
    """
    human_rights = "human_rights"
    """
    Rights everyone holds.
    """
    environmental_sustainability = "environmental_sustainability"
    """
    Natural resources and emissions.
    """
    economic = "economic"
    """
    Jobs, access to finance, taxes and trade.
    """
    government = "government"
    """
    Lawmaking, political falsehoods, defence of the state and the courts.
    """
    culture_and_values = "culture_and_values"
    """
    What a society holds to, and the biases a system can feed.
    """
    other = "other"
    """
    An area the organization names for itself.
    """


class AimsImpactDirection(str, Enum):
    """
    Whether an impact helps or harms.
    """
    positive = "positive"
    """
    It helps.
    """
    negative = "negative"
    """
    It harms.
    """


class AimsResourceProvider(str, Enum):
    """
    Who provides a resource an AI system draws on.
    """
    organization = "organization"
    """
    The organization itself.
    """
    customer = "customer"
    """
    One of its customers.
    """
    third_party = "third_party"
    """
    Someone else.
    """


class AimsDataCategory(str, Enum):
    """
    The parts data can play in machine learning.
    """
    training = "training"
    """
    Data a model learns from.
    """
    validation = "validation"
    """
    Data used to tune a model and compare versions of it.
    """
    test = "test"
    """
    Data held back to see how a finished model does.
    """
    production = "production"
    """
    Data a system meets in service.
    """


class AimsDataPreparationMethod(str, Enum):
    """
    Common ways of making data ready for AI: those the guidance names, and other.
    """
    statistical_exploration = "statistical_exploration"
    """
    Looking at how the values are spread, and describing them.
    """
    cleaning = "cleaning"
    """
    Mending wrong values and dealing with gaps.
    """
    imputation = "imputation"
    """
    Filling gaps by a method.
    """
    normalization = "normalization"
    """
    Reshaping values to a common distribution or range.
    """
    scaling = "scaling"
    """
    Bringing values to comparable sizes.
    """
    labelling = "labelling"
    """
    Marking the values a model is to predict.
    """
    encoding = "encoding"
    """
    Turning categories into numbers.
    """
    other = "other"
    """
    A method the organization names for itself.
    """


class AimsAiThreat(str, Enum):
    """
    Threats to information security peculiar to AI: those the guidance names, and other.
    """
    data_poisoning = "data_poisoning"
    """
    Slipping bad data in to spoil what a model learns.
    """
    model_stealing = "model_stealing"
    """
    Copying a model by querying it or by taking it.
    """
    model_inversion = "model_inversion"
    """
    Working back from a model to the data it learned from.
    """
    other = "other"
    """
    A threat the organization names for itself.
    """


class AimsImplementationStatus(str, Enum):
    """
    How far a control or a plan has been put into effect.
    """
    not_started = "not_started"
    """
    Nothing has been done yet.
    """
    planned = "planned"
    """
    The work is planned, with a timeline.
    """
    in_progress = "in_progress"
    """
    The work is under way.
    """
    implemented = "implemented"
    """
    The work is done and in operation.
    """


class AimsRiskTreatmentOption(str, Enum):
    """
    The ways of treating a risk, by the names ISO 31000 gives them.
    """
    modify = "modify"
    """
    Change the risk with controls that lower its likelihood or its consequences.
    """
    retain = "retain"
    """
    Keep the risk as it is, with management's approval.
    """
    avoid = "avoid"
    """
    Remove the risk by stopping or changing what gives rise to it.
    """
    share = "share"
    """
    Share the risk with another party, such as an insurer or a supplier.
    """


class AimsRiskLevel(str, Enum):
    """
    A five-point scale of risk level, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the organization.
    """
    very_low = "very_low"
    """
    Small enough to need no action.
    """
    low = "low"
    """
    Managed by routine procedures.
    """
    medium = "medium"
    """
    Needs management's attention and planned controls.
    """
    high = "high"
    """
    Needs treatment first and escalation.
    """
    critical = "critical"
    """
    Threatens the organization's objectives and needs action at once.
    """


class AimsLikelihood(str, Enum):
    """
    A five-point scale of likelihood, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the organization.
    """
    rare = "rare"
    """
    Not expected to happen.
    """
    unlikely = "unlikely"
    """
    Could happen, but is not expected to.
    """
    possible = "possible"
    """
    Might happen at some point.
    """
    likely = "likely"
    """
    Will probably happen.
    """
    almost_certain = "almost_certain"
    """
    Expected to happen.
    """


class AimsConsequence(str, Enum):
    """
    A five-point scale of consequence, for an organization that adopts it. ISO/IEC 42001 leaves the scale to the organization.
    """
    negligible = "negligible"
    """
    No noticeable effect.
    """
    minor = "minor"
    """
    An effect normal operations absorb.
    """
    moderate = "moderate"
    """
    An effect that needs management to step in.
    """
    major = "major"
    """
    A serious effect on people, objectives or reputation.
    """
    severe = "severe"
    """
    An effect that threatens lives or the organization's survival.
    """


class AimsDocumentKind(str, Enum):
    """
    The kinds of documented information an AimsDocumentedInformation record holds. Policies have records of their own.
    """
    procedure = "procedure"
    """
    The steps for carrying out an activity the same way each time.
    """
    standard = "standard"
    """
    Mandatory requirements for a technology or a process.
    """
    guideline = "guideline"
    """
    Recommended practice that supports a policy or a procedure.
    """
    record = "record"
    """
    Evidence of what was done or achieved.
    """
    plan = "plan"
    """
    How the organization means to reach an objective.
    """
    report = "report"
    """
    The formal output of an assessment, audit or review.
    """


class AimsAuditType(str, Enum):
    """
    Who carries out an audit, relative to the organization audited, as ISO 19011 sorts audits.
    """
    first_party = "first_party"
    """
    The organization audits itself, or someone audits it on its behalf.
    """
    second_party = "second_party"
    """
    A party with an interest in the organization audits it, such as a customer.
    """
    third_party = "third_party"
    """
    An independent body audits it, such as a certification body or a regulator.
    """


class AimsAuditFindingType(str, Enum):
    """
    The kinds of audit finding.
    """
    major_nonconformity = "major_nonconformity"
    """
    A requirement not met in a way that puts the system's results in doubt.
    """
    minor_nonconformity = "minor_nonconformity"
    """
    A requirement not met in an isolated way that leaves its results in reach.
    """
    observation = "observation"
    """
    A condition that could lead to a nonconformity if left alone.
    """
    positive_finding = "positive_finding"
    """
    Evidence of practice that works well.
    """


class AimsIncidentCategory(str, Enum):
    """
    What an incident involving an AI system concerns. ISO/IEC 42001 tells apart an incident of the system itself from one about security of information or about privacy.
    """
    ai_system = "ai_system"
    """
    The system itself misbehaved or failed.
    """
    information_security = "information_security"
    """
    Information was exposed, altered or made unavailable.
    """
    privacy = "privacy"
    """
    Personal data was exposed or misused.
    """
    safety = "safety"
    """
    Someone or something was put in danger.
    """
    other = "other"
    """
    Something the organization names for itself.
    """


class AimsManagementSystemStandard(str, Enum):
    """
    Management system standards Annex D names as ones to run this system beside, and other.
    """
    iso_iec_27001 = "iso_iec_27001"
    """
    Managing information security.
    """
    iso_iec_27701 = "iso_iec_27701"
    """
    Managing privacy of information.
    """
    iso_9001 = "iso_9001"
    """
    Managing quality.
    """
    iso_22000 = "iso_22000"
    """
    Managing food safety.
    """
    iso_13485 = "iso_13485"
    """
    Managing quality of medical devices.
    """
    other = "other"
    """
    Another management system standard, generic or for one sector.
    """



class AimsRecordMixin(ConfiguredBaseModel):
    """
    What every record of the system has, so that other records can refer to it: an identifier, a title and a description.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ['It is a mixin, not a base class, so that the adapt copy can '
                      "re-root some record classes on LOKF's Concept and leave the "
                      "others as they are. lokf adapt replaces aims_id with LOKF's id, "
                      'and a class that declares id itself must descend from Concept.'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'mixin': True,
         'slot_usage': {'title': {'name': 'title',
                                  'pattern': '^\\s*\\S',
                                  'required': True}}})

    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsDocumentControlMixin(ConfiguredBaseModel):
    """
    The control that documented information is kept under: who wrote, owns and approved it, when it takes effect and is reviewed, how it is classified, kept and changed, and whether it came from outside.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.5'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_documented_information'],
         'mixin': True})

    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })


class AimsManagementSystem(AimsRecordMixin):
    """
    One organization's management system for AI: its scope and context, and every record it keeps, each kind in a list of its own.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.4'}},
         'close_mappings': ['iso27001:IsmsManagementSystem'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core'],
         'mixins': ['AimsRecordMixin'],
         'tree_root': True})

    aims_organization: Optional[AimsOrganization] = Field(default=None, description="""The organization that runs the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_top_management: Optional[str] = Field(default=None, description="""The person or group that runs the organization from the very top.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_governing_body: Optional[str] = Field(default=None, description="""The body top management answers to, such as a board, where there is one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_leadership_evidence: Optional[list[str]] = Field(default=None, description="""What shows that top management leads and commits to the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.1'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_scope: Optional[str] = Field(default=None, description="""How far the system reaches, in the organization's words.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.3'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_scope_boundaries: Optional[list[str]] = Field(default=None, description="""Where the system stops.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.3'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_scope_applicability: Optional[list[str]] = Field(default=None, description="""What in the organization's work the system applies to.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.3'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_processes: Optional[str] = Field(default=None, description="""The processes the system needs and how they work together.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.4'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_internal_issues: Optional[list[str]] = Field(default=None, description="""The matters inside the organization that bear on the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_external_issues: Optional[list[str]] = Field(default=None, description="""The matters outside the organization that bear on the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_planned_changes: Optional[list[str]] = Field(default=None, description="""The changes to the system that are planned.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '6.3'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_external_services: Optional[list[str]] = Field(default=None, description="""What the system takes from outside the organization and keeps under control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.1'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_integrated_standards: Optional[list[AimsManagementSystemStandard]] = Field(default=None, description="""Other standards for management systems that this one is run beside.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_d_item': {'tag': 'annex_d_item', 'value': 'D.2'}},
         'domain_of': ['AimsManagementSystem']} })
    aims_certification_status: Optional[str] = Field(default=None, description="""Where the system stands with certification, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_certification_body: Optional[str] = Field(default=None, description="""The body that certifies the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_certification_date: Optional[date] = Field(default=None, description="""When the system was certified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_recertification_date: Optional[date] = Field(default=None, description="""When the system is next due for recertification.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_interested_parties: Optional[list[AimsInterestedParty]] = Field(default=None, description="""The interested parties the system takes into account.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_policy: Optional[AimsPolicy] = Field(default=None, description="""The AI policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_topic_specific_policies: Optional[list[AimsTopicSpecificPolicy]] = Field(default=None, description="""The policies on single topics under the AI policy.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_roles: Optional[list[AimsRole]] = Field(default=None, description="""The roles that carry the system's duties and powers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_objectives: Optional[list[AimsObjective]] = Field(default=None, description="""The AI objectives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_planned_actions: Optional[list[AimsPlannedAction]] = Field(default=None, description="""The actions planned on risks and opportunities.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_risk_assessment_process: Optional[AimsRiskAssessmentProcess] = Field(default=None, description="""The process for assessing AI risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_risk_treatment_process: Optional[AimsRiskTreatmentProcess] = Field(default=None, description="""The process for treating AI risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_impact_assessment_process: Optional[AimsImpactAssessmentProcess] = Field(default=None, description="""The process for assessing what AI systems may do to people and society.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_risk_assessments: Optional[list[AimsRiskAssessment]] = Field(default=None, description="""The risk assessments carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_risks: Optional[list[AimsRisk]] = Field(default=None, description="""The risks identified, the risk register.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_risk_treatment_plans: Optional[list[AimsRiskTreatmentPlan]] = Field(default=None, description="""The risk treatment plans.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_impact_assessments: Optional[list[AimsImpactAssessment]] = Field(default=None, description="""The impact assessments carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_statement_of_applicability: Optional[AimsStatementOfApplicability] = Field(default=None, description="""The Statement of Applicability.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_controls: Optional[list[AimsControl]] = Field(default=None, description="""The controls the organization has determined it needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_systems: Optional[list[AimsAiSystem]] = Field(default=None, description="""The AI systems the management system covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_system_resources: Optional[list[Union[AimsComponentResource,AimsDataResource,AimsToolingResource,AimsComputingResource,AimsHumanResource]]] = Field(default=None, description="""The resources those AI systems draw on, each told apart by its type.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_development_processes: Optional[list[AimsDevelopmentProcess]] = Field(default=None, description="""The processes for designing and building AI systems responsibly.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_use_processes: Optional[list[AimsResponsibleUseProcess]] = Field(default=None, description="""The processes for using AI systems responsibly.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_technical_documentation: Optional[list[AimsTechnicalDocumentation]] = Field(default=None, description="""The technical documents kept for AI systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_user_information: Optional[list[AimsUserInformation]] = Field(default=None, description="""What users of AI systems are told.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_incident_communication_plans: Optional[list[AimsIncidentCommunicationPlan]] = Field(default=None, description="""The plans for telling users about incidents.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_reporting_obligations: Optional[list[AimsReportingObligation]] = Field(default=None, description="""What the organization must report to others about AI systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_third_party_relationships: Optional[list[Union[AimsThirdPartyRelationship,AimsSupplierRelationship,AimsCustomerRelationship]]] = Field(default=None, description="""The relationships with partners, suppliers, buyers and others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_resources: Optional[list[AimsResource]] = Field(default=None, description="""The resources provided for the management system itself.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_competence_records: Optional[list[AimsCompetenceRecord]] = Field(default=None, description="""The records of competence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_awareness_programme: Optional[AimsAwarenessProgramme] = Field(default=None, description="""The awareness programme.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_communication_plan: Optional[AimsCommunicationPlan] = Field(default=None, description="""The plan for communication about the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_documented_information: Optional[list[AimsDocumentedInformation]] = Field(default=None, description="""The documented information the system keeps that no more specific list holds, such as procedures, plans and reports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_operational_procedures: Optional[list[AimsOperationalProcedure]] = Field(default=None, description="""The procedures for planning and running operations.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_monitoring_programme: Optional[AimsMonitoringProgramme] = Field(default=None, description="""The programme of monitoring and measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_audit_programmes: Optional[list[AimsAuditProgramme]] = Field(default=None, description="""The audit programmes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_audits: Optional[list[AimsAudit]] = Field(default=None, description="""The audits of the system, internal and external.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_management_reviews: Optional[list[AimsManagementReview]] = Field(default=None, description="""The management reviews.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_nonconformities: Optional[list[AimsNonconformity]] = Field(default=None, description="""The nonconformities found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_corrective_actions: Optional[list[AimsCorrectiveAction]] = Field(default=None, description="""The corrective actions taken.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_improvements: Optional[list[AimsImprovementOpportunity]] = Field(default=None, description="""The opportunities for improvement identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_system_events: Optional[list[Union[AimsSystemEvent,AimsIncident]]] = Field(default=None, description="""The events reported about AI systems, the incidents among them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_concern_reporting_process: Optional[AimsConcernReportingProcess] = Field(default=None, description="""The way people raise worries about the organization's part in AI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_concern_reports: Optional[list[AimsConcernReport]] = Field(default=None, description="""The worries people have raised.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementSystem']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsOrganization(AimsRecordMixin):
    """
    The organization that runs the system, with what it needs to know about itself to understand its context and the parts it plays with AI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'close_mappings': ['iso27001:IsmsOrganization', 'spdx_core:Organization'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core'],
         'mixins': ['AimsRecordMixin']})

    aims_organization_legal_name: Optional[str] = Field(default=None, description="""The organization's registered legal name.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOrganization']} })
    aims_organization_trading_names: Optional[list[str]] = Field(default=None, description="""Other names the organization trades under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOrganization']} })
    aims_organization_kind: Optional[str] = Field(default=None, description="""What kind of organization it is, such as a company, an agency or a charity.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOrganization']} })
    aims_organization_sectors: Optional[list[str]] = Field(default=None, description="""The sectors the organization works in, such as health or finance.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_d_item': {'tag': 'annex_d_item', 'value': 'D.1'}},
         'domain_of': ['AimsOrganization']} })
    aims_organization_size: Optional[str] = Field(default=None, description="""How the organization classes its own size.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOrganization']} })
    aims_organization_employee_count: Optional[int] = Field(default=None, description="""About how many people the organization employs.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOrganization']} })
    aims_organization_locations: Optional[list[str]] = Field(default=None, description="""The countries or regions the organization works in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOrganization']} })
    aims_organization_jurisdictions: Optional[list[str]] = Field(default=None, description="""The jurisdictions whose laws and regulations apply to the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOrganization']} })
    aims_organization_parent: Optional[str] = Field(default=None, description="""The organization's parent, if it has one.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOrganization']} })
    aims_organization_subsidiaries: Optional[list[str]] = Field(default=None, description="""The organization's subsidiaries, if it has any.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOrganization']} })
    aims_organization_ai_roles: Optional[list[AimsAiRole]] = Field(default=None, description="""The parts the organization plays towards its AI systems.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'domain_of': ['AimsOrganization']} })
    aims_organization_pii_roles: Optional[list[AimsPiiRole]] = Field(default=None, description="""The parts the organization plays when its AI systems process personal data.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'domain_of': ['AimsOrganization']} })
    aims_organization_climate_change_relevant: Optional[bool] = Field(default=None, description="""Whether the organization has found climate change to matter for the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'domain_of': ['AimsOrganization']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsInterestedParty(AimsRecordMixin):
    """
    A person or organization whose needs and expectations bear on the system, or who may feel its decisions, inside the organization or outside it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.2'}},
         'close_mappings': ['iso27001:IsmsInterestedParty'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core'],
         'mixins': ['AimsRecordMixin']})

    aims_party_category: Optional[str] = Field(default=None, description="""What kind of interested party it is, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsInterestedParty']} })
    aims_party_ai_roles: Optional[list[AimsAiRole]] = Field(default=None, description="""The parts the party plays towards the organization's AI systems.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsInterestedParty']} })
    aims_party_relationship: Optional[str] = Field(default=None, description="""How the party relates to the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsInterestedParty']} })
    aims_party_requirements: Optional[list[str]] = Field(default=None, description="""The party's requirements that bear on the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsInterestedParty']} })
    aims_party_addressed_requirements: Optional[list[str]] = Field(default=None, description="""Which of those requirements the system addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsInterestedParty']} })
    aims_party_climate_change_requirements: Optional[list[str]] = Field(default=None, description="""The party's requirements that concern climate change.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.2'}},
         'domain_of': ['AimsInterestedParty']} })
    aims_party_communication_needs: Optional[str] = Field(default=None, description="""What the party needs to be told, and how.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsInterestedParty']} })
    aims_party_contact: Optional[str] = Field(default=None, description="""How to reach the party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsInterestedParty']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsPolicy(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The AI policy that top management sets: the organization's commitments and the frame for its AI objectives.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.2.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.2'}},
         'close_mappings': ['iso27001:IsmsPolicy'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_cited_clauses: Optional[list[AimsClause]] = Field(default=None, description="""The clauses of the standard the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsDocumentedInformation',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_cited_annex_a_controls: Optional[list[AimsAnnexAControl]] = Field(default=None, description="""The controls of Annex A the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsTopicSpecificPolicy',
                       'AimsControl',
                       'AimsDocumentedInformation',
                       'AimsOperationalProcedure',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_policy_statement: Optional[str] = Field(default=None, description="""The policy's own statement, in the organization's words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy']} })
    aims_policy_objectives_framework: Optional[str] = Field(default=None, description="""How the policy frames the setting of AI objectives.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.2'}},
         'domain_of': ['AimsPolicy']} })
    aims_policy_commitments: Optional[list[str]] = Field(default=None, description="""The commitments the policy makes, at least to meeting requirements and to improving.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.2'}},
         'domain_of': ['AimsPolicy']} })
    aims_policy_principles: Optional[list[str]] = Field(default=None, description="""The principles that guide what the organization does with AI.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.2.2'}},
         'domain_of': ['AimsPolicy']} })
    aims_policy_exceptions_process: Optional[str] = Field(default=None, description="""How departures from the policy are handled.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.2.2'}},
         'domain_of': ['AimsPolicy']} })
    aims_policy_influences: Optional[list[str]] = Field(default=None, description="""What shaped the policy, such as strategy, values, the law or the risks.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.2.2'}},
         'domain_of': ['AimsPolicy']} })
    aims_policy_related_policies: Optional[list[str]] = Field(default=None, description="""The organization's other policies this one refers to or touches.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.2.3'},
                         'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.2'}},
         'domain_of': ['AimsPolicy']} })
    aims_policy_communication_date: Optional[date] = Field(default=None, description="""When the policy was made known inside the organization.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.2'}},
         'domain_of': ['AimsPolicy']} })
    aims_policy_availability: Optional[str] = Field(default=None, description="""How interested parties can get the policy, where that is fitting.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.2'}},
         'domain_of': ['AimsPolicy']} })
    aims_policy_review_role: Optional[str] = Field(default=None, description="""The role management approved to develop, review and evaluate the policy.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.2.4'}},
         'domain_of': ['AimsPolicy']} })
    aims_policy_review_interval: Optional[str] = Field(default=None, description="""How often the policy is reviewed, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.2.4'}},
         'domain_of': ['AimsPolicy']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsTopicSpecificPolicy(AimsDocumentControlMixin, AimsRecordMixin):
    """
    A policy on one topic that gives more guidance under the AI policy, such as assessing impacts or building systems.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.2.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_annex_a', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsTopicSpecificPolicy',
                       'AimsObjective',
                       'AimsControl',
                       'AimsAiSystem',
                       'AimsOperationalProcedure']} })
    aims_cited_annex_a_controls: Optional[list[AimsAnnexAControl]] = Field(default=None, description="""The controls of Annex A the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsTopicSpecificPolicy',
                       'AimsControl',
                       'AimsDocumentedInformation',
                       'AimsOperationalProcedure',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_topic_policy_topic: Optional[str] = Field(default=None, description="""The topic the policy covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsTopicSpecificPolicy']} })
    aims_topic_policy_parent: Optional[str] = Field(default=None, description="""The AI policy this policy supports.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsTopicSpecificPolicy']} })
    aims_topic_policy_audience: Optional[str] = Field(default=None, description="""Whom the policy is written for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsTopicSpecificPolicy']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsRole(AimsRecordMixin):
    """
    A role in the system, with the duties and powers it carries and who holds it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.3.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.3'}},
         'close_mappings': ['iso27001:IsmsRole', 'oscal:Role'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core'],
         'mixins': ['AimsRecordMixin']})

    aims_role_category: Optional[str] = Field(default=None, description="""What kind of role it is, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRole']} })
    aims_role_areas: Optional[list[str]] = Field(default=None, description="""The areas the role covers, such as privacy, safety or human oversight.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.3.2'}},
         'domain_of': ['AimsRole']} })
    aims_role_responsibilities: Optional[list[str]] = Field(default=None, description="""The duties assigned to the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRole']} })
    aims_role_authorities: Optional[list[str]] = Field(default=None, description="""The powers the role carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRole']} })
    aims_role_ensures_conformity: Optional[bool] = Field(default=None, description="""Whether the role sees that the system meets the standard.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.3'}},
         'domain_of': ['AimsRole']} })
    aims_role_reports_performance: Optional[bool] = Field(default=None, description="""Whether the role tells top management how the system is doing.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '5.3'}},
         'domain_of': ['AimsRole']} })
    aims_role_accountability: Optional[str] = Field(default=None, description="""What the role is accountable for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRole']} })
    aims_role_holders: Optional[list[str]] = Field(default=None, description="""The people who hold the role.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRole']} })
    aims_role_delegation: Optional[str] = Field(default=None, description="""How the role may delegate its duties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRole']} })
    aims_role_reports_to: Optional[str] = Field(default=None, description="""The role this role reports to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRole']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsObjective(AimsRecordMixin):
    """
    An AI objective: a result the organization aims for, with how it plans to reach it and how it judges progress.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '6.2'}},
         'close_mappings': ['iso27001:IsmsObjective'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core'],
         'mixins': ['AimsRecordMixin']})

    aims_responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective',
                       'AimsPlannedAction',
                       'AimsIncludedControl',
                       'AimsCommunication',
                       'AimsMonitoringItem',
                       'AimsCorrectiveAction',
                       'AimsImprovementOpportunity']} })
    aims_relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsTopicSpecificPolicy',
                       'AimsObjective',
                       'AimsControl',
                       'AimsAiSystem',
                       'AimsOperationalProcedure']} })
    aims_objective_categories: Optional[list[AimsObjectiveCategory]] = Field(default=None, description="""The kinds of objective the record bears on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective', 'AimsControl']} })
    aims_objective_purpose: Optional[AimsObjectivePurpose] = Field(default=None, description="""What the objective is for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_statement: Optional[str] = Field(default=None, description="""The objective, as the organization states it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_target: Optional[str] = Field(default=None, description="""The value the objective aims for, where it can be measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_current_value: Optional[str] = Field(default=None, description="""The value last measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_metric: Optional[str] = Field(default=None, description="""How the objective's value is defined.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_measurement_method: Optional[str] = Field(default=None, description="""How the value is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_measurement_frequency: Optional[str] = Field(default=None, description="""How often the value is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_target_date: Optional[date] = Field(default=None, description="""When the objective is to be reached.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_achievement: Optional[str] = Field(default=None, description="""How far the objective has been reached, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_risks: Optional[list[str]] = Field(default=None, description="""The risks that help or hinder the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_action_plan: Optional[str] = Field(default=None, description="""The steps that lead to the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_resources: Optional[str] = Field(default=None, description="""The resources needed to reach the objective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_evaluation: Optional[str] = Field(default=None, description="""How the outcome will be judged.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_objective_communication: Optional[str] = Field(default=None, description="""How the objective is made known.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsPlannedAction(AimsRecordMixin):
    """
    An action planned on a risk or an opportunity the system faces, with how it fits the system's processes and how its effect will be judged.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.1'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_risk_management'],
         'mixins': ['AimsRecordMixin']})

    aims_responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective',
                       'AimsPlannedAction',
                       'AimsIncludedControl',
                       'AimsCommunication',
                       'AimsMonitoringItem',
                       'AimsCorrectiveAction',
                       'AimsImprovementOpportunity']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_planned_action_risks: Optional[list[str]] = Field(default=None, description="""The risks the action addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction']} })
    aims_planned_action_opportunities: Optional[list[str]] = Field(default=None, description="""The opportunities the action addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction']} })
    aims_planned_action_integration: Optional[str] = Field(default=None, description="""How the action fits into the system's processes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction']} })
    aims_planned_action_effectiveness: Optional[str] = Field(default=None, description="""How the action's effect will be judged.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsRiskAssessmentProcess(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The organization's process for assessing AI risks: its criteria, scales and method, and when it runs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.2'}},
         'close_mappings': ['iso27001:IsmsRiskAssessmentProcess'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_risk_management', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_risk_criteria: Optional[list[str]] = Field(default=None, description="""The criteria for AI risk, which tell acceptable risk from the rest and steer assessment, treatment and the weighing of impacts.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.1'}},
         'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_risk_policy_alignment: Optional[str] = Field(default=None, description="""How the process follows the AI policy and the AI objectives.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_risk_comparability: Optional[str] = Field(default=None, description="""How the process keeps repeated assessments consistent and comparable.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_risk_method: Optional[str] = Field(default=None, description="""The method used to identify, analyse and evaluate risks.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_risk_likelihood_scale: Optional[str] = Field(default=None, description="""The scale for rating likelihood.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_risk_consequence_scale: Optional[str] = Field(default=None, description="""The scale for rating consequences.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_risk_matrix: Optional[str] = Field(default=None, description="""How likelihood and consequence combine into a risk level.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_risk_prioritization: Optional[str] = Field(default=None, description="""How the assessed risks are ranked for treatment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_risk_assessment_interval: Optional[str] = Field(default=None, description="""How often risks are assessed, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.2'}},
         'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_risk_assessment_triggers: Optional[list[str]] = Field(default=None, description="""The changes that start an assessment outside the schedule.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.2'}},
         'domain_of': ['AimsRiskAssessmentProcess']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsRiskAssessment(AimsDocumentControlMixin, AimsRecordMixin):
    """
    One risk assessment carried out under the process, and what it found.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.2'}},
         'close_mappings': ['iso27001:IsmsRiskAssessment'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_risk_management'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_assessment_scope: Optional[str] = Field(default=None, description="""What the assessment covered.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessment']} })
    aims_assessment_date: Optional[date] = Field(default=None, description="""When the assessment was carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessment']} })
    aims_assessment_assessor: Optional[str] = Field(default=None, description="""Who carried out the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessment']} })
    aims_assessment_method_used: Optional[str] = Field(default=None, description="""The method this assessment applied.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessment']} })
    aims_assessment_risks: Optional[list[str]] = Field(default=None, description="""The risks the assessment identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessment']} })
    aims_assessment_impact_assessments: Optional[list[str]] = Field(default=None, description="""The impact assessments the assessment drew on.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.2, 6.1.4'}},
         'domain_of': ['AimsRiskAssessment']} })
    aims_assessment_summary: Optional[str] = Field(default=None, description="""A summary of what the assessment found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessment']} })
    aims_assessment_recommendations: Optional[list[str]] = Field(default=None, description="""What the assessment recommends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessment']} })
    aims_assessment_next_date: Optional[date] = Field(default=None, description="""When the next assessment is planned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskAssessment']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsRisk(AimsRecordMixin):
    """
    An AI risk in the risk register: where it comes from, which objectives it helps or hinders, who could feel its consequences, how it is rated and how it is treated.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.2'}},
         'close_mappings': ['iso27001:IsmsRisk'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_risk_management'],
         'mixins': ['AimsRecordMixin'],
         'related_mappings': ['nist_ai_100_1:Risk']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_risk_source_categories: Optional[list[AimsRiskSourceCategory]] = Field(default=None, description="""The kinds of risk source the record bears on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk', 'AimsControl']} })
    aims_risk_source: Optional[str] = Field(default=None, description="""Where the risk comes from, in the organization's words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_objectives: Optional[list[str]] = Field(default=None, description="""The AI objectives the risk helps or hinders.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_consequences_for_organization: Optional[str] = Field(default=None, description="""What the organization could suffer if the risk came about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_consequences_for_individuals: Optional[str] = Field(default=None, description="""What persons could suffer if the risk came about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_consequences_for_societies: Optional[str] = Field(default=None, description="""What society could suffer if the risk came about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_owner: Optional[str] = Field(default=None, description="""The person who is accountable for the risk and has the authority to manage it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_likelihood: Optional[AimsLikelihood] = Field(default=None, description="""How likely the risk is, where that can be judged.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_consequence: Optional[AimsConsequence] = Field(default=None, description="""How severe the consequences would be.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_inherent_level: Optional[AimsRiskLevel] = Field(default=None, description="""The risk's level before controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_existing_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls already acting on the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_residual_level: Optional[AimsRiskLevel] = Field(default=None, description="""The risk's level after controls.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_acceptable: Optional[bool] = Field(default=None, description="""Whether the risk is acceptable under the organization's criteria.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.1'}},
         'domain_of': ['AimsRisk']} })
    aims_risk_treatment_option: Optional[AimsRiskTreatmentOption] = Field(default=None, description="""The treatment chosen for the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_treatment_priority: Optional[str] = Field(default=None, description="""How soon the risk is to be treated, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk']} })
    aims_risk_impact_assessments: Optional[list[str]] = Field(default=None, description="""The impact assessments that inform the risk.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsRisk']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsRiskTreatmentProcess(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The organization's process for treating AI risks: how it chooses options and controls, checks them against Annex A and produces the Statement of Applicability and the plan.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'close_mappings': ['iso27001:IsmsRiskTreatmentProcess'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_risk_management', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_treatment_options_guidance: Optional[str] = Field(default=None, description="""How a treatment option is chosen for a risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentProcess']} })
    aims_treatment_control_selection: Optional[str] = Field(default=None, description="""How the controls a treatment needs are chosen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentProcess']} })
    aims_treatment_annex_a_comparison: Optional[str] = Field(default=None, description="""How the chosen controls are compared with Annex A, so that none is missed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentProcess']} })
    aims_treatment_additional_controls: Optional[str] = Field(default=None, description="""How the organization decides it needs controls beyond Annex A, and where it gets them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentProcess']} })
    aims_treatment_annex_b_use: Optional[str] = Field(default=None, description="""How the guidance of Annex B is taken into account.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentProcess']} })
    aims_treatment_soa_template: Optional[str] = Field(default=None, description="""The template the Statement of Applicability follows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentProcess']} })
    aims_treatment_approval_workflow: Optional[str] = Field(default=None, description="""How designated management approves a plan and accepts the risk left over.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentProcess']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsRiskTreatmentPlan(AimsDocumentControlMixin, AimsRecordMixin):
    """
    A plan to treat one or more risks: the actions and controls, who carries them out and when, and designated management's approval of the plan and of the risk left over.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3, 8.3'}},
         'close_mappings': ['iso27001:IsmsRiskTreatmentPlan'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_risk_management', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_implementation_state: Optional[AimsImplementationStatus] = Field(default=None, description="""How far the control or the plan has been put into effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan', 'AimsIncludedControl', 'AimsControl']} })
    aims_plan_scope: Optional[str] = Field(default=None, description="""What the plan covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_risks: Optional[list[str]] = Field(default=None, description="""The risks the plan treats.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_actions: Optional[list[str]] = Field(default=None, description="""The actions the plan takes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_controls: Optional[list[str]] = Field(default=None, description="""The controls the plan puts in place.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_resources: Optional[str] = Field(default=None, description="""The resources the plan needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_responsible_parties: Optional[list[str]] = Field(default=None, description="""Who carries out the plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_timeline: Optional[str] = Field(default=None, description="""When the plan's actions are to happen.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_approver: Optional[str] = Field(default=None, description="""The designated management that approved the plan.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_residual_risk_acceptance: Optional[str] = Field(default=None, description="""How that management accepted the risk left over.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_effectiveness: Optional[str] = Field(default=None, description="""What the check on whether the plan works found.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.3'}},
         'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_revalidation: Optional[str] = Field(default=None, description="""How options that did not work were reviewed, and what changed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.3'}},
         'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_plan_completion_date: Optional[date] = Field(default=None, description="""When the plan was completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsImpactAssessmentProcess(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The process for working out what AI systems may do to people and society: when it applies, what it takes in, who runs it and how the results are used.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.5.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_risk_management', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_impact_process_triggers: Optional[list[str]] = Field(default=None, description="""What calls for an assessment, such as how critical the use is or a large change.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.4'}},
         'domain_of': ['AimsImpactAssessmentProcess']} })
    aims_impact_process_interval: Optional[str] = Field(default=None, description="""How often assessments run, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.4'}},
         'domain_of': ['AimsImpactAssessmentProcess']} })
    aims_impact_process_steps: Optional[list[str]] = Field(default=None, description="""The steps of an assessment, from finding impacts to reporting them.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.2'}},
         'domain_of': ['AimsImpactAssessmentProcess']} })
    aims_impact_process_assessors: Optional[str] = Field(default=None, description="""Who carries out an assessment.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.2'}},
         'domain_of': ['AimsImpactAssessmentProcess']} })
    aims_impact_process_use: Optional[str] = Field(default=None, description="""How results feed risk assessments and a system's design or use.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsImpactAssessmentProcess']} })
    aims_impact_process_subjects: Optional[list[AimsImpactSubject]] = Field(default=None, description="""Who the process looks at.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImpactAssessmentProcess']} })
    aims_impact_process_areas: Optional[list[AimsImpactArea]] = Field(default=None, description="""The areas of impact the process looks at.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item',
                                          'value': 'B.5.4, B.5.5'}},
         'domain_of': ['AimsImpactAssessmentProcess']} })
    aims_impact_process_retention: Optional[str] = Field(default=None, description="""How long results are kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.5.3'}},
         'domain_of': ['AimsImpactAssessmentProcess']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsImpactAssessment(AimsDocumentControlMixin, AimsRecordMixin):
    """
    One impact assessment carried out under the process: the systems and the setting it looked at, and each impact it found.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.5.3'},
                         'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4, 8.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_risk_management', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_impact_scope: Optional[str] = Field(default=None, description="""What the assessment covered.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImpactAssessment']} })
    aims_impact_discipline: Optional[str] = Field(default=None, description="""The discipline it was carried out for, if it was only one, such as privacy or safety.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_date: Optional[date] = Field(default=None, description="""When the assessment was carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImpactAssessment']} })
    aims_impact_assessor: Optional[str] = Field(default=None, description="""Who carried out the assessment.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImpactAssessment']} })
    aims_impact_intended_use: Optional[str] = Field(default=None, description="""What the system is for.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.3'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_foreseeable_misuse: Optional[str] = Field(default=None, description="""How the system could predictably be misused.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.3'},
                         'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_technical_context: Optional[str] = Field(default=None, description="""The technical setting the system runs in.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_societal_context: Optional[str] = Field(default=None, description="""The social setting the system runs in.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_jurisdictions: Optional[list[str]] = Field(default=None, description="""The jurisdictions that apply to where the system runs.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_demographic_groups: Optional[list[str]] = Field(default=None, description="""The groups of people the system is meant for or touches.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.3'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_system_complexity: Optional[str] = Field(default=None, description="""How complex the system is.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.3'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_human_role: Optional[str] = Field(default=None, description="""What part people play beside the system, and their means of oversight.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.3'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_failures: Optional[list[str]] = Field(default=None, description="""The failures that can be foreseen, their effects and what limits them.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.3'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_workforce: Optional[str] = Field(default=None, description="""What the system means for jobs and the skills of staff.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.5.3'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_findings: Optional[list[AimsIdentifiedImpact]] = Field(default=None, description="""The impacts the assessment found.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.5.4, A.5.5'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_shared_with: Optional[list[str]] = Field(default=None, description="""The interested parties told of the result.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsImpactAssessment']} })
    aims_impact_next_date: Optional[date] = Field(default=None, description="""When the next assessment is planned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImpactAssessment']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsIdentifiedImpact(ConfiguredBaseModel):
    """
    One impact an assessment found: on whom it falls, in what area, whether it helps or harms, and what limits the harm.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.5.4, A.5.5'}},
         'close_mappings': ['nist_ai_100_1:Impact'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_risk_management']})

    aims_identified_impact_subject: AimsImpactSubject = Field(default=..., description="""Who the impact falls on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIdentifiedImpact']} })
    aims_identified_impact_area: Optional[AimsImpactArea] = Field(default=None, description="""The area the impact falls in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIdentifiedImpact']} })
    aims_identified_impact_direction: Optional[AimsImpactDirection] = Field(default=None, description="""Whether the impact helps or harms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIdentifiedImpact']} })
    aims_identified_impact_text: str = Field(default=..., description="""What the impact is, in the organization's words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIdentifiedImpact']} })
    aims_identified_impact_mitigation: Optional[list[str]] = Field(default=None, description="""What is done to limit the harm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIdentifiedImpact']} })

    @field_validator('aims_identified_impact_text')
    def pattern_aims_identified_impact_text(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid aims_identified_impact_text format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid aims_identified_impact_text format: {v}"
            raise ValueError(err_msg)
        return v


class AimsStatementOfApplicability(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The Statement of Applicability: each control the organization needs, with why it is included and whether it is in place, and each control it leaves out, with why.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'close_mappings': ['iso27001:IsmsStatementOfApplicability'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_annex_a', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_soa_entries: Optional[list[Union[AimsIncludedControl,AimsExcludedControl]]] = Field(default=None, description="""The statement's entries, one for each control included or left out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsStatementOfApplicability']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsApplicabilityEntry(ConfiguredBaseModel):
    """
    One entry of the Statement of Applicability, which either includes a control or leaves one out, and says why.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'close_mappings': ['iso27001:IsmsApplicabilityEntry'],
         'comments': ['An entry may hold for the whole system or for particular AI '
                      'systems, which aims_ai_systems names.'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_annex_a'],
         'slot_usage': {'aims_entry_type': {'name': 'aims_entry_type',
                                            'required': True}}})

    aims_entry_type: Literal["AimsApplicabilityEntry"] = Field(default="AimsApplicabilityEntry", description="""The kind of entry, AimsIncludedControl or AimsExcludedControl.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsApplicabilityEntry']} })
    aims_entry_annex_a_control: Optional[AimsAnnexAControl] = Field(default=None, description="""The Annex A control a Statement of Applicability entry concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsApplicabilityEntry']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_entry_justification: str = Field(default=..., description="""Why the control is included or left out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsApplicabilityEntry']} })

    @field_validator('aims_entry_justification')
    def pattern_aims_entry_justification(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid aims_entry_justification format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid aims_entry_justification format: {v}"
            raise ValueError(err_msg)
        return v


class AimsIncludedControl(AimsApplicabilityEntry):
    """
    An entry that includes a control the organization needs, from Annex A or from elsewhere, says which risks call for it and whether it is in place.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'any_of': [{'slot_conditions': {'aims_entry_annex_a_control': {'name': 'aims_entry_annex_a_control',
                                                                        'required': True}}},
                    {'slot_conditions': {'aims_included_control': {'name': 'aims_included_control',
                                                                   'required': True}}}],
         'close_mappings': ['iso27001:IsmsIncludedControl'],
         'comments': ['An included control names an Annex A control, one of the '
                      "organization's controls, or both."],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_annex_a'],
         'slot_usage': {'aims_implementation_state': {'name': 'aims_implementation_state',
                                                      'required': True}}})

    aims_implementation_state: AimsImplementationStatus = Field(default=..., description="""How far the control or the plan has been put into effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan', 'AimsIncludedControl', 'AimsControl']} })
    aims_responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective',
                       'AimsPlannedAction',
                       'AimsIncludedControl',
                       'AimsCommunication',
                       'AimsMonitoringItem',
                       'AimsCorrectiveAction',
                       'AimsImprovementOpportunity']} })
    aims_included_control: Optional[str] = Field(default=None, description="""The organization's control the entry includes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncludedControl']} })
    aims_included_risks: Optional[list[str]] = Field(default=None, description="""The risks the control answers to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncludedControl']} })
    aims_included_evidence: Optional[str] = Field(default=None, description="""What shows that the control is in place.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncludedControl']} })
    aims_included_target_date: Optional[date] = Field(default=None, description="""When the control is to be in place, if it is not yet.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncludedControl']} })
    aims_entry_type: Literal["AimsIncludedControl"] = Field(default="AimsIncludedControl", description="""The kind of entry, AimsIncludedControl or AimsExcludedControl.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsApplicabilityEntry']} })
    aims_entry_annex_a_control: Optional[AimsAnnexAControl] = Field(default=None, description="""The Annex A control a Statement of Applicability entry concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsApplicabilityEntry']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_entry_justification: str = Field(default=..., description="""Why the control is included or left out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsApplicabilityEntry']} })

    @field_validator('aims_entry_justification')
    def pattern_aims_entry_justification(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid aims_entry_justification format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid aims_entry_justification format: {v}"
            raise ValueError(err_msg)
        return v


class AimsExcludedControl(AimsApplicabilityEntry):
    """
    An entry that leaves out an Annex A control the organization does not need, and says why.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'close_mappings': ['iso27001:IsmsExcludedControl'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_annex_a'],
         'slot_usage': {'aims_entry_annex_a_control': {'name': 'aims_entry_annex_a_control',
                                                       'required': True}}})

    aims_entry_type: Literal["AimsExcludedControl"] = Field(default="AimsExcludedControl", description="""The kind of entry, AimsIncludedControl or AimsExcludedControl.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsApplicabilityEntry']} })
    aims_entry_annex_a_control: AimsAnnexAControl = Field(default=..., description="""The Annex A control a Statement of Applicability entry concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsApplicabilityEntry']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_entry_justification: str = Field(default=..., description="""Why the control is included or left out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsApplicabilityEntry']} })

    @field_validator('aims_entry_justification')
    def pattern_aims_entry_justification(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid aims_entry_justification format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid aims_entry_justification format: {v}"
            raise ValueError(err_msg)
        return v


class AimsControl(AimsRecordMixin):
    """
    A control the organization has found it needs to treat its risks: what it does in the organization's words, which Annex A controls it answers to, who owns it, how far it is in place and how well it works.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.3'}},
         'close_mappings': ['iso27001:IsmsControl'],
         'comments': ["The text and guidance are the organization's own words, never "
                      'the text of ISO/IEC 42001. A control from another source names '
                      'no Annex A control.'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_annex_a'],
         'mixins': ['AimsRecordMixin'],
         'related_mappings': ['oscal:Control']})

    aims_relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsTopicSpecificPolicy',
                       'AimsObjective',
                       'AimsControl',
                       'AimsAiSystem',
                       'AimsOperationalProcedure']} })
    aims_implementation_state: Optional[AimsImplementationStatus] = Field(default=None, description="""How far the control or the plan has been put into effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRiskTreatmentPlan', 'AimsIncludedControl', 'AimsControl']} })
    aims_cited_annex_a_controls: Optional[list[AimsAnnexAControl]] = Field(default=None, description="""The controls of Annex A the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsTopicSpecificPolicy',
                       'AimsControl',
                       'AimsDocumentedInformation',
                       'AimsOperationalProcedure',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_objective_categories: Optional[list[AimsObjectiveCategory]] = Field(default=None, description="""The kinds of objective the record bears on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective', 'AimsControl']} })
    aims_risk_source_categories: Optional[list[AimsRiskSourceCategory]] = Field(default=None, description="""The kinds of risk source the record bears on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRisk', 'AimsControl']} })
    aims_control_area: Optional[AimsControlArea] = Field(default=None, description="""Which of Annex A's nine areas the control belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsControl']} })
    aims_control_text: Optional[str] = Field(default=None, description="""What the control does, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsControl']} })
    aims_control_guidance: Optional[str] = Field(default=None, description="""The organization's notes on putting the control in place.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsControl']} })
    aims_control_owner: Optional[str] = Field(default=None, description="""The person who owns the control.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsControl']} })
    aims_control_implementation_date: Optional[date] = Field(default=None, description="""When the control was put in place.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsControl']} })
    aims_control_effectiveness: Optional[str] = Field(default=None, description="""How well the control works, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.1'}},
         'domain_of': ['AimsControl']} })
    aims_control_last_tested: Optional[date] = Field(default=None, description="""When the control was last tested.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsControl']} })
    aims_control_evidence: Optional[list[str]] = Field(default=None, description="""Where the evidence that the control is in place is kept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsControl']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsAiSystem(AimsRecordMixin):
    """
    One AI system under the management system: what it is for, how it is built, run and overseen, what it draws on, and what is kept about it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.2'},
                         'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'close_mappings': ['nist_ai_100_1:AiSystem'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records'],
         'mixins': ['AimsRecordMixin']})

    aims_relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsTopicSpecificPolicy',
                       'AimsObjective',
                       'AimsControl',
                       'AimsAiSystem',
                       'AimsOperationalProcedure']} })
    aims_system_intended_purpose: Optional[str] = Field(default=None, description="""What the system is for.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_intended_uses: Optional[list[str]] = Field(default=None, description="""The uses the system is meant for.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.9.4'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_foreseeable_misuse: Optional[list[str]] = Field(default=None, description="""The ways people could predictably misuse the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_domain: Optional[str] = Field(default=None, description="""The field the system is applied in.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.1'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_deployment_context: Optional[str] = Field(default=None, description="""The setting the system runs in.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '6.1.4'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_life_cycle_stage: Optional[AimsLifecycleStage] = Field(default=None, description="""The stage of its life the system is in now.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAiSystem']} })
    aims_system_organization_roles: Optional[list[AimsAiRole]] = Field(default=None, description="""The parts the organization plays towards this system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '4.1'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_pii_roles: Optional[list[AimsPiiRole]] = Field(default=None, description="""The parts the organization plays when this system processes personal data.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.2'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_rationale: Optional[str] = Field(default=None, description="""Why the system is being built, such as a business case or a customer's request.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.2'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_requirements: Optional[list[str]] = Field(default=None, description="""What the system must meet, across its whole life.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.2'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_ml_approach: Optional[str] = Field(default=None, description="""The machine learning approach it takes, such as supervised or unsupervised.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.3'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_model_types: Optional[list[str]] = Field(default=None, description="""The learning algorithms and kinds of model it uses.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.3'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_continuous_learning: Optional[bool] = Field(default=None, description="""Whether what it meets in service goes on changing its behaviour.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.6'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_automation_level: Optional[str] = Field(default=None, description="""How much the system does without people.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_c_item': {'tag': 'annex_c_item', 'value': 'C.3.3'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_threats: Optional[list[AimsAiThreat]] = Field(default=None, description="""The threats peculiar to AI that were considered for the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item',
                                          'value': 'B.6.2.3, B.6.2.6'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_verification_measures: Optional[list[str]] = Field(default=None, description="""The tests, data and methods used to verify and validate the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.4'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_evaluation_criteria: Optional[list[str]] = Field(default=None, description="""What the system is judged against, such as a limit on its errors.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.4'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_release_criteria: Optional[list[str]] = Field(default=None, description="""What must hold before the system is released.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.5'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_deployment_plan: Optional[str] = Field(default=None, description="""The documented information that holds the plan for putting it into service.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.5'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_operation_elements: Optional[list[str]] = Field(default=None, description="""What keeping the system in service takes, such as watching, repairs and updates.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.6'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_performance_metrics: Optional[list[str]] = Field(default=None, description="""The measures of how the system does in service, with acceptable values.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.6'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_log_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of its life at which the system keeps event logs.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.8'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_log_contents: Optional[list[str]] = Field(default=None, description="""What the logs record, such as times of use or out-of-range results.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.8'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_log_retention: Optional[str] = Field(default=None, description="""How long the logs are kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.8'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_human_oversight_required: Optional[bool] = Field(default=None, description="""Whether the system may be used only with people watching over it.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.9.3'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_human_oversight: Optional[str] = Field(default=None, description="""How people watch over the system, and who may overrule it.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.9.3'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_human_oversight_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of its life at which people watch over the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.9.3'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_resources_used: Optional[list[str]] = Field(default=None, description="""The resources the system draws on.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.4.2'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_technical_documents: Optional[list[str]] = Field(default=None, description="""The technical documents kept for the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.7'}},
         'domain_of': ['AimsAiSystem']} })
    aims_system_impact_assessments: Optional[list[str]] = Field(default=None, description="""The impact assessments of the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAiSystem']} })
    aims_system_relationships: Optional[list[str]] = Field(default=None, description="""The partners, suppliers and customers that deal with the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.10.2'}},
         'domain_of': ['AimsAiSystem']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsSystemResource(AimsRecordMixin):
    """
    Something an AI system draws on, told apart by its type, with the stages of the system's life that need it and who provides it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.4.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records'],
         'mixins': ['AimsRecordMixin'],
         'slot_usage': {'aims_resource_type': {'name': 'aims_resource_type',
                                               'required': True}}})

    aims_resource_type: Literal["AimsSystemResource"] = Field(default="AimsSystemResource", description="""The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsSystemResource']} })
    aims_life_cycle_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of an AI system's life the record applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemResource', 'AimsThirdPartyRelationship']} })
    aims_resource_provider: Optional[AimsResourceProvider] = Field(default=None, description="""Who provides the resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.2'}},
         'domain_of': ['AimsSystemResource']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsComponentResource(AimsSystemResource):
    """
    A part of a system, and how it is joined to the rest.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records']})

    aims_component_kind: Optional[str] = Field(default=None, description="""What kind of part it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsComponentResource']} })
    aims_component_integration: Optional[str] = Field(default=None, description="""How the part is joined to the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.3'}},
         'domain_of': ['AimsComponentResource']} })
    aims_resource_type: Literal["AimsComponentResource"] = Field(default="AimsComponentResource", description="""The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsSystemResource']} })
    aims_life_cycle_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of an AI system's life the record applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemResource', 'AimsThirdPartyRelationship']} })
    aims_resource_provider: Optional[AimsResourceProvider] = Field(default=None, description="""Who provides the resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.2'}},
         'domain_of': ['AimsSystemResource']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsDataResource(AimsSystemResource):
    """
    Data an AI system draws on: where it came from, what part it plays, how it was obtained, made ready and judged fit, and how long it is kept.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.4.3, A.7.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records']})

    aims_data_categories: Optional[list[AimsDataCategory]] = Field(default=None, description="""The parts the data plays in machine learning.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_kinds: Optional[list[str]] = Field(default=None, description="""What kind of data it is, in a classification the organization names.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_intended_use: Optional[str] = Field(default=None, description="""What the data is for.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_quantity: Optional[str] = Field(default=None, description="""How much data is needed.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.7.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_sources: Optional[list[str]] = Field(default=None, description="""Where the data comes from, such as bought, shared, open or synthetic.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.7.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_source_characteristics: Optional[list[str]] = Field(default=None, description="""How the source behaves, such as fixed, streamed or made by machine.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.7.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_subject_demographics: Optional[list[str]] = Field(default=None, description="""Who the data is about, with any known bias or systematic error.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.7.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_prior_handling: Optional[str] = Field(default=None, description="""What was done with the data before, such as earlier uses.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.7.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_rights: Optional[list[str]] = Field(default=None, description="""The rights bearing on the data, such as personal data or copyright.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.7.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_metadata: Optional[list[str]] = Field(default=None, description="""The metadata that comes with it, such as details of labelling.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.7.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_provenance: Optional[str] = Field(default=None, description="""The record of where the data came from and what happened to it.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.7.5'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_provenance_verification: Optional[str] = Field(default=None, description="""How that record is checked, where it needs to be.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.7.5'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_quality_requirements: Optional[list[str]] = Field(default=None, description="""What quality the data must have.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.7.4'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_quality_results: Optional[list[str]] = Field(default=None, description="""How the data measures up to those requirements.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.7.4'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_bias_issues: Optional[list[str]] = Field(default=None, description="""Known or suspected bias in the data.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item',
                                          'value': 'B.4.3, B.7.4'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_representativeness: Optional[str] = Field(default=None, description="""How well training data stands for what the system will meet in service.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.7.2'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_labelling_process: Optional[str] = Field(default=None, description="""How the data is labelled.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_preparation_criteria: Optional[str] = Field(default=None, description="""What decides how the data is made ready.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.7.6'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_preparation_methods: Optional[list[AimsDataPreparationMethod]] = Field(default=None, description="""The methods used to make the data ready.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.7.6'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_last_updated: Optional[date] = Field(default=None, description="""When the data last changed.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_retention: Optional[str] = Field(default=None, description="""How long the data is kept and how it is disposed of.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.3'}},
         'domain_of': ['AimsDataResource']} })
    aims_data_classification: Optional[str] = Field(default=None, description="""The information classification the data carries.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDataResource']} })
    aims_resource_type: Literal["AimsDataResource"] = Field(default="AimsDataResource", description="""The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsSystemResource']} })
    aims_life_cycle_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of an AI system's life the record applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemResource', 'AimsThirdPartyRelationship']} })
    aims_resource_provider: Optional[AimsResourceProvider] = Field(default=None, description="""Who provides the resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.2'}},
         'domain_of': ['AimsSystemResource']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsToolingResource(AimsSystemResource):
    """
    A tool an AI system draws on, such as an algorithm, a model or a development tool.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.4.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records']})

    aims_tool_category: Optional[str] = Field(default=None, description="""What kind of tool it is, such as a model or an evaluation method.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.4'}},
         'domain_of': ['AimsToolingResource']} })
    aims_tool_version: Optional[str] = Field(default=None, description="""The version in use.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsToolingResource']} })
    aims_tool_vendor: Optional[str] = Field(default=None, description="""Who supplies the tool.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsToolingResource']} })
    aims_tool_licence: Optional[str] = Field(default=None, description="""The terms the tool is used under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsToolingResource']} })
    aims_tool_purpose: Optional[str] = Field(default=None, description="""What the tool is used for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsToolingResource']} })
    aims_resource_type: Literal["AimsToolingResource"] = Field(default="AimsToolingResource", description="""The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsSystemResource']} })
    aims_life_cycle_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of an AI system's life the record applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemResource', 'AimsThirdPartyRelationship']} })
    aims_resource_provider: Optional[AimsResourceProvider] = Field(default=None, description="""Who provides the resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.2'}},
         'domain_of': ['AimsSystemResource']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsComputingResource(AimsSystemResource):
    """
    Hardware or computing an AI system draws on: what it needs, where it runs and what the hardware costs.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.4.5'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records']})

    aims_computing_requirements: Optional[str] = Field(default=None, description="""What the system needs in order to run, such as on a small device.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.5'}},
         'domain_of': ['AimsComputingResource']} })
    aims_computing_location: Optional[str] = Field(default=None, description="""Where it runs, such as on the premises, in a cloud or at the edge.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.5'}},
         'domain_of': ['AimsComputingResource']} })
    aims_computing_processing: Optional[str] = Field(default=None, description="""The processing it provides, network and storage included.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.5'}},
         'domain_of': ['AimsComputingResource']} })
    aims_computing_hardware_impact: Optional[str] = Field(default=None, description="""What the hardware costs, in money or to the environment.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.5'}},
         'domain_of': ['AimsComputingResource']} })
    aims_resource_type: Literal["AimsComputingResource"] = Field(default="AimsComputingResource", description="""The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsSystemResource']} })
    aims_life_cycle_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of an AI system's life the record applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemResource', 'AimsThirdPartyRelationship']} })
    aims_resource_provider: Optional[AimsResourceProvider] = Field(default=None, description="""Who provides the resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.2'}},
         'domain_of': ['AimsSystemResource']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsHumanResource(AimsSystemResource):
    """
    People an AI system draws on: their skills and the work they do on it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.4.6'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records']})

    aims_human_role: Optional[str] = Field(default=None, description="""The role these people hold.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsHumanResource']} })
    aims_human_competences: Optional[list[str]] = Field(default=None, description="""The skills they bring.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.4.6'}},
         'domain_of': ['AimsHumanResource']} })
    aims_human_activities: Optional[list[str]] = Field(default=None, description="""The work they do on the system, from building it to decommissioning it.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.4.6'}},
         'domain_of': ['AimsHumanResource']} })
    aims_human_diversity: Optional[str] = Field(default=None, description="""How the team's range of expertise was considered.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.6'}},
         'domain_of': ['AimsHumanResource']} })
    aims_resource_type: Literal["AimsHumanResource"] = Field(default="AimsHumanResource", description="""The kind of resource: AimsComponentResource, AimsDataResource, AimsToolingResource, AimsComputingResource or AimsHumanResource.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsSystemResource']} })
    aims_life_cycle_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of an AI system's life the record applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemResource', 'AimsThirdPartyRelationship']} })
    aims_resource_provider: Optional[AimsResourceProvider] = Field(default=None, description="""Who provides the resource.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.4.2'}},
         'domain_of': ['AimsSystemResource']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsDevelopmentProcess(AimsDocumentControlMixin, AimsRecordMixin):
    """
    A process for designing and building an AI system responsibly: the life cycle it follows, and what it asks of testing, oversight, data and approvals.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.1.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_development_life_cycle_model: Optional[str] = Field(default=None, description="""The life cycle model followed, which may be the organization's own.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_testing: Optional[str] = Field(default=None, description="""What must be tested and how.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_human_oversight: Optional[str] = Field(default=None, description="""What oversight by people is asked for, with its tools and processes.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_impact_assessment_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages at which impact assessments run.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_training_data_rules: Optional[str] = Field(default=None, description="""What data may be used, from which suppliers, and how it is labelled.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_expertise: Optional[str] = Field(default=None, description="""The expertise or training developers need.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_release_criteria: Optional[list[str]] = Field(default=None, description="""What must hold before a release.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_approvals: Optional[list[str]] = Field(default=None, description="""Who must approve what, at each stage.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_change_control: Optional[str] = Field(default=None, description="""How changes are controlled.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_usability: Optional[str] = Field(default=None, description="""What is asked of how easy the system is to use and how far people stay in control.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_development_party_engagement: Optional[str] = Field(default=None, description="""How interested parties are brought in.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.1.3'}},
         'domain_of': ['AimsDevelopmentProcess']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsResponsibleUseProcess(AimsDocumentControlMixin, AimsRecordMixin):
    """
    A process for using AI systems responsibly: what decides if a system may be used, built in-house or brought in.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.9.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_use_approvals: Optional[list[str]] = Field(default=None, description="""The approvals needed before use.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.9.2'}},
         'domain_of': ['AimsResponsibleUseProcess']} })
    aims_use_costs: Optional[str] = Field(default=None, description="""What use costs, ongoing upkeep included.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.9.2'}},
         'domain_of': ['AimsResponsibleUseProcess']} })
    aims_use_sourcing_requirements: Optional[list[str]] = Field(default=None, description="""What a system or its supplier must meet to be taken on.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.9.2'}},
         'domain_of': ['AimsResponsibleUseProcess']} })
    aims_use_legal_requirements: Optional[list[str]] = Field(default=None, description="""The laws that bear on use.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.9.2'}},
         'domain_of': ['AimsResponsibleUseProcess']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsTechnicalDocumentation(AimsDocumentControlMixin, AimsRecordMixin):
    """
    Technical documents about an AI system for one kind of reader: what they hold, and the form they take.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.7'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_technical_doc_audiences: Optional[list[str]] = Field(default=None, description="""Who the documents are for, such as users or a supervisory authority.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.7'}},
         'domain_of': ['AimsTechnicalDocumentation']} })
    aims_technical_doc_form: Optional[str] = Field(default=None, description="""The form the documents take for those readers.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.6.2.7'}},
         'domain_of': ['AimsTechnicalDocumentation']} })
    aims_technical_doc_contents: Optional[list[str]] = Field(default=None, description="""What the documents hold, such as limits, design choices or test records.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.7'}},
         'domain_of': ['AimsTechnicalDocumentation']} })
    aims_technical_doc_failure_plan: Optional[str] = Field(default=None, description="""How failures are managed, such as rolling back or turning features off.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.6.2.7'}},
         'domain_of': ['AimsTechnicalDocumentation']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsUserInformation(AimsDocumentControlMixin, AimsRecordMixin):
    """
    What those who use a system are told: the contents, how it reaches them, what decided it, and the check that they got it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.8.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_user_information_contents: Optional[list[str]] = Field(default=None, description="""What users are told, such as that AI is behind what they see and how to overrule it.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.2'}},
         'domain_of': ['AimsUserInformation']} })
    aims_user_information_channels: Optional[list[str]] = Field(default=None, description="""How it reaches them, such as instructions, alerts or a web page.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.2'}},
         'domain_of': ['AimsUserInformation']} })
    aims_user_information_criteria: Optional[list[str]] = Field(default=None, description="""What decided what they are told.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.2'}},
         'domain_of': ['AimsUserInformation']} })
    aims_user_information_validated: Optional[bool] = Field(default=None, description="""Whether the organization has checked that users can get it and that it is right.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.2'}},
         'domain_of': ['AimsUserInformation']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsIncidentCommunicationPlan(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The plan for telling users when a system goes wrong: which incidents, how soon, to which authorities, and with what details.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.8.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_incident_plan_categories: Optional[list[AimsIncidentCategory]] = Field(default=None, description="""The kinds of incident the plan covers.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.4'}},
         'domain_of': ['AimsIncidentCommunicationPlan']} })
    aims_incident_plan_timeline: Optional[str] = Field(default=None, description="""How soon people must be told.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.4'}},
         'domain_of': ['AimsIncidentCommunicationPlan']} })
    aims_incident_plan_authorities: Optional[list[str]] = Field(default=None, description="""The authorities that must be told, if any.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.4'}},
         'domain_of': ['AimsIncidentCommunicationPlan']} })
    aims_incident_plan_details: Optional[list[str]] = Field(default=None, description="""What each notice must say.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.4'}},
         'domain_of': ['AimsIncidentCommunicationPlan']} })
    aims_incident_plan_integration: Optional[str] = Field(default=None, description="""How the plan fits the organization's wider handling of incidents.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.4'}},
         'domain_of': ['AimsIncidentCommunicationPlan']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsReportingObligation(AimsRecordMixin):
    """
    Something the organization must report about a system to an interested party: to whom, under what rule, what and how soon.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.8.5'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records'],
         'mixins': ['AimsRecordMixin']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_obligation_parties: Optional[list[str]] = Field(default=None, description="""Who must be told.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsReportingObligation']} })
    aims_obligation_basis: Optional[str] = Field(default=None, description="""The law or agreement that creates the duty.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsReportingObligation']} })
    aims_obligation_jurisdiction: Optional[str] = Field(default=None, description="""The jurisdiction the duty arises in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsReportingObligation']} })
    aims_obligation_contents: Optional[list[str]] = Field(default=None, description="""What must be reported, such as risks, assessments or logs.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.5'}},
         'domain_of': ['AimsReportingObligation']} })
    aims_obligation_timeframe: Optional[str] = Field(default=None, description="""How soon it must be reported.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.5'}},
         'domain_of': ['AimsReportingObligation']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsResource(AimsRecordMixin):
    """
    A resource provided for the management system itself, such as people, time, tools or budget. What an AI system draws on is an AimsSystemResource.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.1'}},
         'close_mappings': ['iso27001:IsmsResource'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core'],
         'mixins': ['AimsRecordMixin']})

    aims_support_category: Optional[str] = Field(default=None, description="""What kind of resource it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsResource']} })
    aims_support_quantity: Optional[str] = Field(default=None, description="""How much of the resource is provided.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsResource']} })
    aims_support_allocation_date: Optional[date] = Field(default=None, description="""When the resource was allocated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsResource']} })
    aims_support_allocated_to: Optional[str] = Field(default=None, description="""What the resource is allocated to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsResource']} })
    aims_support_cost: Optional[str] = Field(default=None, description="""What the resource costs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsResource']} })
    aims_support_availability: Optional[str] = Field(default=None, description="""Whether the resource is available now, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsResource']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsCompetenceRecord(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The evidence of one person's competence for work that affects AI performance, and what is done to close any gap.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.2'}},
         'close_mappings': ['iso27001:IsmsCompetenceRecord'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_competence_person: Optional[str] = Field(default=None, description="""The person the record is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCompetenceRecord']} })
    aims_competence_role: Optional[str] = Field(default=None, description="""The role the person holds.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCompetenceRecord']} })
    aims_competence_required: Optional[list[str]] = Field(default=None, description="""The competences the role needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCompetenceRecord']} })
    aims_competence_education: Optional[list[str]] = Field(default=None, description="""The person's relevant education.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCompetenceRecord']} })
    aims_competence_training: Optional[list[str]] = Field(default=None, description="""The training the person has completed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCompetenceRecord']} })
    aims_competence_experience: Optional[list[str]] = Field(default=None, description="""The person's relevant experience.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCompetenceRecord']} })
    aims_competence_assessment_date: Optional[date] = Field(default=None, description="""When the person's competence was last assessed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCompetenceRecord']} })
    aims_competence_gaps: Optional[list[str]] = Field(default=None, description="""The gaps the assessment found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCompetenceRecord']} })
    aims_competence_actions: Optional[list[str]] = Field(default=None, description="""What is done to close the gaps, and how well it worked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCompetenceRecord']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsAwarenessProgramme(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The programme that tells people working for the organization about the AI policy, their part in the system and what failing it would mean.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.3'}},
         'close_mappings': ['iso27001:IsmsAwarenessProgramme'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_awareness_topics: Optional[list[str]] = Field(default=None, description="""The topics the programme covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAwarenessProgramme']} })
    aims_awareness_methods: Optional[list[str]] = Field(default=None, description="""How the programme is delivered.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAwarenessProgramme']} })
    aims_awareness_audience: Optional[str] = Field(default=None, description="""Whom the programme is for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAwarenessProgramme']} })
    aims_awareness_frequency: Optional[str] = Field(default=None, description="""How often the programme runs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAwarenessProgramme']} })
    aims_awareness_completion_tracking: Optional[str] = Field(default=None, description="""How completion is tracked.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAwarenessProgramme']} })
    aims_awareness_effectiveness: Optional[str] = Field(default=None, description="""How the programme's effect is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAwarenessProgramme']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsCommunicationPlan(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The plan for communication about the system, inside the organization and outside it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.4'}},
         'close_mappings': ['iso27001:IsmsCommunicationPlan'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_communication_items: Optional[list[AimsCommunication]] = Field(default=None, description="""The communications the plan provides for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCommunicationPlan']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsCommunication(ConfiguredBaseModel):
    """
    One communication the plan provides for: what about, to whom, when, how, and who communicates.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.4'}},
         'close_mappings': ['iso27001:IsmsCommunication'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_core']})

    aims_responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective',
                       'AimsPlannedAction',
                       'AimsIncludedControl',
                       'AimsCommunication',
                       'AimsMonitoringItem',
                       'AimsCorrectiveAction',
                       'AimsImprovementOpportunity']} })
    aims_communication_subject: str = Field(default=..., description="""What the communication is about.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCommunication']} })
    aims_communication_purpose: Optional[str] = Field(default=None, description="""Why it is communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCommunication']} })
    aims_communication_audience: Optional[str] = Field(default=None, description="""To whom it is communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCommunication']} })
    aims_communication_external: Optional[bool] = Field(default=None, description="""Whether it goes outside the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCommunication']} })
    aims_communication_timing: Optional[str] = Field(default=None, description="""When it is communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCommunication']} })
    aims_communication_method: Optional[str] = Field(default=None, description="""How it is communicated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCommunication']} })
    aims_communication_records_required: Optional[bool] = Field(default=None, description="""Whether a record of the communication is kept.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCommunication']} })


class AimsDocumentedInformation(AimsDocumentControlMixin, AimsRecordMixin):
    """
    A document or record the system keeps under control that no more specific record describes, such as a procedure, a plan or a report.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '7.5'}},
         'close_mappings': ['iso27001:IsmsDocumentedInformation'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_cited_clauses: Optional[list[AimsClause]] = Field(default=None, description="""The clauses of the standard the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsDocumentedInformation',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_cited_annex_a_controls: Optional[list[AimsAnnexAControl]] = Field(default=None, description="""The controls of Annex A the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsTopicSpecificPolicy',
                       'AimsControl',
                       'AimsDocumentedInformation',
                       'AimsOperationalProcedure',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_document_kind: AimsDocumentKind = Field(default=..., description="""What kind of documented information it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentedInformation']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsOperationalProcedure(AimsDocumentControlMixin, AimsRecordMixin):
    """
    A procedure by which the organization plans and controls the processes that meet its requirements, such as managing data for building or vetting suppliers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '8.1'}},
         'close_mappings': ['iso27001:IsmsOperationalProcedure'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_relevant_controls: Optional[list[str]] = Field(default=None, description="""The organization's controls that the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsTopicSpecificPolicy',
                       'AimsObjective',
                       'AimsControl',
                       'AimsAiSystem',
                       'AimsOperationalProcedure']} })
    aims_cited_annex_a_controls: Optional[list[AimsAnnexAControl]] = Field(default=None, description="""The controls of Annex A the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsTopicSpecificPolicy',
                       'AimsControl',
                       'AimsDocumentedInformation',
                       'AimsOperationalProcedure',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_procedure_scope: Optional[str] = Field(default=None, description="""What the procedure covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOperationalProcedure']} })
    aims_procedure_criteria: Optional[str] = Field(default=None, description="""The criteria the processes are run to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOperationalProcedure']} })
    aims_procedure_control_measures: Optional[list[str]] = Field(default=None, description="""The measures that control the processes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOperationalProcedure']} })
    aims_procedure_roles: Optional[list[str]] = Field(default=None, description="""The roles that carry out the procedure.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOperationalProcedure']} })
    aims_procedure_change_control: Optional[str] = Field(default=None, description="""How planned changes are controlled, and unplanned ones reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsOperationalProcedure']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsMonitoringProgramme(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The programme that watches, measures, analyses and judges how well the system does and how well it works.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.1'}},
         'close_mappings': ['iso27001:IsmsMonitoringProgramme'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_performance_evaluation', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_monitoring_items: Optional[list[AimsMonitoringItem]] = Field(default=None, description="""What the programme monitors and measures.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringProgramme']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsMonitoringItem(ConfiguredBaseModel):
    """
    One thing the monitoring programme measures: what, how, how often and by whom it is measured and analysed, and against what thresholds.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.1'}},
         'close_mappings': ['iso27001:IsmsMonitoringItem'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_performance_evaluation']})

    aims_responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective',
                       'AimsPlannedAction',
                       'AimsIncludedControl',
                       'AimsCommunication',
                       'AimsMonitoringItem',
                       'AimsCorrectiveAction',
                       'AimsImprovementOpportunity']} })
    aims_monitoring_metric: str = Field(default=..., description="""The name of what is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })
    aims_monitoring_description: Optional[str] = Field(default=None, description="""What the measurement shows.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })
    aims_monitoring_method: Optional[str] = Field(default=None, description="""How it is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })
    aims_monitoring_frequency: Optional[str] = Field(default=None, description="""How often it is measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })
    aims_monitoring_analysis_frequency: Optional[str] = Field(default=None, description="""How often the results are analysed and evaluated.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })
    aims_monitoring_analyst: Optional[str] = Field(default=None, description="""Who analyses and evaluates the results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })
    aims_monitoring_target: Optional[str] = Field(default=None, description="""The value aimed for.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })
    aims_monitoring_alert_threshold: Optional[str] = Field(default=None, description="""The value that calls for action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })
    aims_monitoring_current_value: Optional[str] = Field(default=None, description="""The value last measured.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })
    aims_monitoring_trend: Optional[str] = Field(default=None, description="""Which way the value is moving.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsMonitoringItem']} })


class AimsAuditProgramme(AimsDocumentControlMixin, AimsRecordMixin):
    """
    A programme of internal audits: the audits planned over a period, how often and why, and the resources and auditors they need.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.2.2'}},
         'close_mappings': ['iso27001:IsmsAuditProgramme'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_performance_evaluation', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_programme_period: Optional[str] = Field(default=None, description="""The period the programme covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditProgramme']} })
    aims_programme_audits: Optional[list[str]] = Field(default=None, description="""The audits the programme plans.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditProgramme']} })
    aims_programme_frequency_rationale: Optional[str] = Field(default=None, description="""Why the audits happen as often as they do, given what matters most and past results.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditProgramme']} })
    aims_programme_methods: Optional[str] = Field(default=None, description="""How the audits are carried out.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditProgramme']} })
    aims_programme_responsibilities: Optional[list[str]] = Field(default=None, description="""Who answers for planning, running and reporting them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditProgramme']} })
    aims_programme_resources: Optional[str] = Field(default=None, description="""The resources the programme needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditProgramme']} })
    aims_programme_auditor_selection: Optional[str] = Field(default=None, description="""How auditors are chosen so that they stay objective and impartial.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditProgramme']} })
    aims_programme_status: Optional[str] = Field(default=None, description="""Where the programme stands, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditProgramme']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsAudit(AimsDocumentControlMixin, AimsRecordMixin):
    """
    An audit of the system: an internal audit, or one by a customer or a certification body, with its scope, criteria, team, findings and conclusion.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.2'}},
         'close_mappings': ['iso27001:IsmsAudit'],
         'comments': ['A combined audit of several management systems at once lists '
                      'each standard in aims_audit_standards.'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_performance_evaluation', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_audit_type: AimsAuditType = Field(default=..., description="""Who carries out the audit, relative to the organization.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_standards: Optional[list[AimsManagementSystemStandard]] = Field(default=None, description="""Other standards for management systems the audit covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_scope: Optional[str] = Field(default=None, description="""What the audit covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_criteria: Optional[list[str]] = Field(default=None, description="""What the audit compares the system against.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_objectives: Optional[list[str]] = Field(default=None, description="""What the audit sets out to establish.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_period_start: Optional[date] = Field(default=None, description="""When the audit began.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_period_end: Optional[date] = Field(default=None, description="""When the audit ended.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_lead: Optional[str] = Field(default=None, description="""Who led the audit.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_team: Optional[list[str]] = Field(default=None, description="""Who else audited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_auditees: Optional[list[str]] = Field(default=None, description="""Who represented the parts of the organization audited.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_plan: Optional[str] = Field(default=None, description="""The documented information that holds the audit plan.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_findings: Optional[list[AimsAuditFinding]] = Field(default=None, description="""What the audit found, good and bad.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_conclusion: Optional[str] = Field(default=None, description="""The audit's overall conclusion.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_report_date: Optional[date] = Field(default=None, description="""When the audit report was issued.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_audit_report_distribution: Optional[list[str]] = Field(default=None, description="""Who received the audit report.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAudit']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsAuditFinding(AimsRecordMixin):
    """
    One finding of an audit: a nonconformity, an observation or a strength, with the requirement or control it concerns, its evidence and how it is closed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.2'}},
         'close_mappings': ['iso27001:IsmsAuditFinding'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_performance_evaluation'],
         'mixins': ['AimsRecordMixin'],
         'rules': [{'description': 'A finding that names a nonconformity record is a '
                                   'finding of a nonconformity.',
                    'postconditions': {'slot_conditions': {'aims_finding_type': {'equals_string_in': ['major_nonconformity',
                                                                                                      'minor_nonconformity'],
                                                                                 'name': 'aims_finding_type'}}},
                    'preconditions': {'slot_conditions': {'aims_finding_nonconformity': {'name': 'aims_finding_nonconformity',
                                                                                         'value_presence': 'PRESENT'}}}}]})

    aims_cited_clauses: Optional[list[AimsClause]] = Field(default=None, description="""The clauses of the standard the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsDocumentedInformation',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_cited_annex_a_controls: Optional[list[AimsAnnexAControl]] = Field(default=None, description="""The controls of Annex A the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsTopicSpecificPolicy',
                       'AimsControl',
                       'AimsDocumentedInformation',
                       'AimsOperationalProcedure',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_finding_type: AimsAuditFindingType = Field(default=..., description="""What kind of finding it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_finding_control: Optional[str] = Field(default=None, description="""The organization's control the finding concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_finding_evidence: Optional[str] = Field(default=None, description="""The objective evidence for the finding.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_finding_root_cause: Optional[str] = Field(default=None, description="""What the analysis of the finding's cause found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_finding_risk: Optional[str] = Field(default=None, description="""What the finding means for risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_finding_recommendation: Optional[str] = Field(default=None, description="""What the auditor recommends.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_finding_auditee_response: Optional[str] = Field(default=None, description="""How the auditee responded.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_finding_corrective_action: Optional[str] = Field(default=None, description="""The corrective action the finding led to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_finding_nonconformity: Optional[str] = Field(default=None, description="""The nonconformity the finding recorded, for a finding of one.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '10.2'}},
         'domain_of': ['AimsAuditFinding']} })
    aims_finding_closure_status: Optional[str] = Field(default=None, description="""Whether the finding is closed, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_finding_closure_date: Optional[date] = Field(default=None, description="""When the finding was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsAuditFinding']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsManagementReview(AimsDocumentControlMixin, AimsRecordMixin):
    """
    A review of the system by top management: what it took in, what it decided and what it asked to be done.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause', 'value': '9.3'}},
         'close_mappings': ['iso27001:IsmsManagementReview'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_performance_evaluation', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_review_held_on: date = Field(default=..., description="""When the review was held.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementReview']} })
    aims_review_attendees: Optional[list[str]] = Field(default=None, description="""Who attended the review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementReview']} })
    aims_review_previous_actions: Optional[str] = Field(default=None, description="""Where the actions from earlier reviews stand.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.3.2'}},
         'domain_of': ['AimsManagementReview']} })
    aims_review_context_changes: Optional[str] = Field(default=None, description="""How the matters that bear on the system have changed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.3.2'}},
         'domain_of': ['AimsManagementReview']} })
    aims_review_interested_party_changes: Optional[str] = Field(default=None, description="""How interested parties' needs and expectations have changed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.3.2'}},
         'domain_of': ['AimsManagementReview']} })
    aims_review_nonconformity_trends: Optional[str] = Field(default=None, description="""How nonconformities and their corrections have been trending.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.3.2'}},
         'domain_of': ['AimsManagementReview']} })
    aims_review_monitoring_trends: Optional[str] = Field(default=None, description="""The trends in what was monitored and measured.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.3.2'}},
         'domain_of': ['AimsManagementReview']} })
    aims_review_audit_trends: Optional[str] = Field(default=None, description="""The trends in audit results.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.3.2'}},
         'domain_of': ['AimsManagementReview']} })
    aims_review_improvement_opportunities: Optional[list[str]] = Field(default=None, description="""The opportunities for improvement raised.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.3.2'}},
         'domain_of': ['AimsManagementReview']} })
    aims_review_decisions: Optional[list[str]] = Field(default=None, description="""What the review decided about improving.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.3.3'}},
         'domain_of': ['AimsManagementReview']} })
    aims_review_system_changes: Optional[list[str]] = Field(default=None, description="""The changes to the system the review found were needed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '9.3.3'}},
         'domain_of': ['AimsManagementReview']} })
    aims_review_actions: Optional[list[str]] = Field(default=None, description="""What the review asked to be done.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementReview']} })
    aims_review_next_date: Optional[date] = Field(default=None, description="""When the next review is planned.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsManagementReview']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsNonconformity(AimsRecordMixin):
    """
    A nonconformity: a requirement not met, how it was found and contained, its consequences and cause, and how it was closed.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '10.2'}},
         'close_mappings': ['iso27001:IsmsNonconformity'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_improvement'],
         'mixins': ['AimsRecordMixin']})

    aims_cited_clauses: Optional[list[AimsClause]] = Field(default=None, description="""The clauses of the standard the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsDocumentedInformation',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_cited_annex_a_controls: Optional[list[AimsAnnexAControl]] = Field(default=None, description="""The controls of Annex A the record answers to or concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPolicy',
                       'AimsTopicSpecificPolicy',
                       'AimsControl',
                       'AimsDocumentedInformation',
                       'AimsOperationalProcedure',
                       'AimsAuditFinding',
                       'AimsNonconformity']} })
    aims_nonconformity_source: Optional[str] = Field(default=None, description="""How the nonconformity came to light, such as an audit, a review or an incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_detected_on: Optional[date] = Field(default=None, description="""When the nonconformity was found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_detected_by: Optional[str] = Field(default=None, description="""Who or what found it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_requirement: Optional[str] = Field(default=None, description="""The requirement not met, of the organization or of an interested party, in words.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_immediate_actions: Optional[list[str]] = Field(default=None, description="""What was done at once to contain and fix it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_consequences: Optional[str] = Field(default=None, description="""How its consequences were dealt with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_root_cause: Optional[str] = Field(default=None, description="""What caused it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_similar_check: Optional[str] = Field(default=None, description="""Whether it could happen, or has happened, elsewhere.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_status: Optional[str] = Field(default=None, description="""Where the nonconformity stands, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_closure_date: Optional[date] = Field(default=None, description="""When it was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_nonconformity_closure_evidence: Optional[str] = Field(default=None, description="""What shows that it is closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsNonconformity']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsCorrectiveAction(AimsRecordMixin):
    """
    An action that removes the cause of one or more nonconformities so that they do not recur, and the check that it worked.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '10.2'}},
         'close_mappings': ['iso27001:IsmsCorrectiveAction'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_improvement'],
         'mixins': ['AimsRecordMixin']})

    aims_responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective',
                       'AimsPlannedAction',
                       'AimsIncludedControl',
                       'AimsCommunication',
                       'AimsMonitoringItem',
                       'AimsCorrectiveAction',
                       'AimsImprovementOpportunity']} })
    aims_action_nonconformities: Optional[list[str]] = Field(default=None, description="""The nonconformities the action addresses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_action_root_cause: Optional[str] = Field(default=None, description="""The cause the action removes.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_action_target_date: Optional[date] = Field(default=None, description="""When the action is to be complete.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_action_completion_date: Optional[date] = Field(default=None, description="""When the action was complete.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_action_resources: Optional[str] = Field(default=None, description="""The resources the action needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_action_effectiveness_criteria: Optional[str] = Field(default=None, description="""How the action's effect will be judged.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_action_effectiveness_review_date: Optional[date] = Field(default=None, description="""When the action's effect was reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_action_effective: Optional[bool] = Field(default=None, description="""Whether the review found the action effective.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_action_system_changes: Optional[str] = Field(default=None, description="""The changes to the system the action needs.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_action_status: Optional[str] = Field(default=None, description="""Where the action stands, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsCorrectiveAction']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsImprovementOpportunity(AimsRecordMixin):
    """
    An opportunity to make the system more suitable, adequate or effective, and what came of it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '10.1'}},
         'close_mappings': ['iso27001:IsmsImprovementOpportunity'],
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_improvement'],
         'mixins': ['AimsRecordMixin']})

    aims_responsible_role: Optional[str] = Field(default=None, description="""The role that answers for the record's activity or outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsObjective',
                       'AimsPlannedAction',
                       'AimsIncludedControl',
                       'AimsCommunication',
                       'AimsMonitoringItem',
                       'AimsCorrectiveAction',
                       'AimsImprovementOpportunity']} })
    aims_improvement_source: Optional[str] = Field(default=None, description="""Where the opportunity came from, such as a review, an audit or daily work.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_improvement_identified_on: Optional[date] = Field(default=None, description="""When the opportunity was identified.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_improvement_identified_by: Optional[str] = Field(default=None, description="""Who identified it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_improvement_benefit: Optional[str] = Field(default=None, description="""What the improvement is expected to bring.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_improvement_priority: Optional[str] = Field(default=None, description="""How soon it is to be acted on, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_improvement_plan: Optional[str] = Field(default=None, description="""How the improvement is to be made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_improvement_target_date: Optional[date] = Field(default=None, description="""When the improvement is to be made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_improvement_completion_date: Optional[date] = Field(default=None, description="""When it was made.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_improvement_outcome: Optional[str] = Field(default=None, description="""What the improvement brought.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_improvement_status: Optional[str] = Field(default=None, description="""Where it stands, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsImprovementOpportunity']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsThirdPartyRelationship(AimsRecordMixin):
    """
    A relationship with another party in an AI system's life, such as a partner: who carries which duty, and what assures the organization of that.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.10.2'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_external_parties'],
         'mixins': ['AimsRecordMixin'],
         'slot_usage': {'aims_relationship_type': {'name': 'aims_relationship_type',
                                                   'required': True}}})

    aims_relationship_type: Literal["AimsThirdPartyRelationship"] = Field(default="AimsThirdPartyRelationship", description="""The kind of record: AimsThirdPartyRelationship, AimsSupplierRelationship or AimsCustomerRelationship.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsThirdPartyRelationship']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_life_cycle_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of an AI system's life the record applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemResource', 'AimsThirdPartyRelationship']} })
    aims_relationship_party: Optional[str] = Field(default=None, description="""The other party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_party_roles: Optional[list[AimsAiRole]] = Field(default=None, description="""The parts the other party plays towards the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_contract: Optional[str] = Field(default=None, description="""The agreement the relationship rests on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_responsibilities: Optional[list[str]] = Field(default=None, description="""The duties each side carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.10.2'}},
         'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_pii_role: Optional[AimsPiiRole] = Field(default=None, description="""The part the other party plays when personal data is processed.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.2'}},
         'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_documentation: Optional[list[str]] = Field(default=None, description="""The documents one side owes the other about the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.2'}},
         'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_assurance_evidence: Optional[list[str]] = Field(default=None, description="""What assures the organization that the party meets its duties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_review_frequency: Optional[str] = Field(default=None, description="""How often the relationship is reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsSupplierRelationship(AimsThirdPartyRelationship):
    """
    A relationship with a supplier to the organization's AI work: what it provides, the risk that brings, and how it is held to the organization's approach.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.10.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_external_parties']})

    aims_supplier_provides: Optional[list[str]] = Field(default=None, description="""What it provides, such as data, models, software or a whole system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.3'}},
         'domain_of': ['AimsSupplierRelationship']} })
    aims_supplier_risk: Optional[AimsRiskLevel] = Field(default=None, description="""How much risk what it provides brings.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.3'}},
         'domain_of': ['AimsSupplierRelationship']} })
    aims_supplier_requirements: Optional[list[str]] = Field(default=None, description="""What the organization asks of the supplier.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.3'}},
         'domain_of': ['AimsSupplierRelationship']} })
    aims_supplier_monitoring: Optional[str] = Field(default=None, description="""How the supplier is watched and judged over time.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.3'}},
         'domain_of': ['AimsSupplierRelationship']} })
    aims_supplier_integration: Optional[str] = Field(default=None, description="""How what it provides is joined to the organization's systems.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.3'}},
         'domain_of': ['AimsSupplierRelationship']} })
    aims_supplier_corrective_actions: Optional[list[str]] = Field(default=None, description="""What the supplier was asked to put right.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.3'}},
         'domain_of': ['AimsSupplierRelationship']} })
    aims_relationship_type: Literal["AimsSupplierRelationship"] = Field(default="AimsSupplierRelationship", description="""The kind of record: AimsThirdPartyRelationship, AimsSupplierRelationship or AimsCustomerRelationship.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsThirdPartyRelationship']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_life_cycle_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of an AI system's life the record applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemResource', 'AimsThirdPartyRelationship']} })
    aims_relationship_party: Optional[str] = Field(default=None, description="""The other party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_party_roles: Optional[list[AimsAiRole]] = Field(default=None, description="""The parts the other party plays towards the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_contract: Optional[str] = Field(default=None, description="""The agreement the relationship rests on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_responsibilities: Optional[list[str]] = Field(default=None, description="""The duties each side carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.10.2'}},
         'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_pii_role: Optional[AimsPiiRole] = Field(default=None, description="""The part the other party plays when personal data is processed.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.2'}},
         'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_documentation: Optional[list[str]] = Field(default=None, description="""The documents one side owes the other about the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.2'}},
         'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_assurance_evidence: Optional[list[str]] = Field(default=None, description="""What assures the organization that the party meets its duties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_review_frequency: Optional[str] = Field(default=None, description="""How often the relationship is reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsCustomerRelationship(AimsThirdPartyRelationship):
    """
    A relationship with a customer of the organization's AI work: what it expects, who answers for what, and which limits it was told of.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.10.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_external_parties']})

    aims_customer_expectations: Optional[list[str]] = Field(default=None, description="""What the customer expects and wants.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.10.4'}},
         'domain_of': ['AimsCustomerRelationship']} })
    aims_customer_agreement: Optional[str] = Field(default=None, description="""The contract or terms of use that apply.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.4'}},
         'domain_of': ['AimsCustomerRelationship']} })
    aims_customer_responsibility_split: Optional[str] = Field(default=None, description="""What the provider answers for, and what the customer answers for.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.4'}},
         'domain_of': ['AimsCustomerRelationship']} })
    aims_customer_communicated_limits: Optional[list[str]] = Field(default=None, description="""What the customer was told the system cannot do, or where it stops being valid.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.4'}},
         'domain_of': ['AimsCustomerRelationship']} })
    aims_relationship_type: Literal["AimsCustomerRelationship"] = Field(default="AimsCustomerRelationship", description="""The kind of record: AimsThirdPartyRelationship, AimsSupplierRelationship or AimsCustomerRelationship.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsThirdPartyRelationship']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_life_cycle_stages: Optional[list[AimsLifecycleStage]] = Field(default=None, description="""The stages of an AI system's life the record applies to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemResource', 'AimsThirdPartyRelationship']} })
    aims_relationship_party: Optional[str] = Field(default=None, description="""The other party.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_party_roles: Optional[list[AimsAiRole]] = Field(default=None, description="""The parts the other party plays towards the system.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_contract: Optional[str] = Field(default=None, description="""The agreement the relationship rests on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_responsibilities: Optional[list[str]] = Field(default=None, description="""The duties each side carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.10.2'}},
         'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_pii_role: Optional[AimsPiiRole] = Field(default=None, description="""The part the other party plays when personal data is processed.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.2'}},
         'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_documentation: Optional[list[str]] = Field(default=None, description="""The documents one side owes the other about the system.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.10.2'}},
         'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_assurance_evidence: Optional[list[str]] = Field(default=None, description="""What assures the organization that the party meets its duties.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_relationship_review_frequency: Optional[str] = Field(default=None, description="""How often the relationship is reviewed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsThirdPartyRelationship']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsSystemEvent(AimsRecordMixin):
    """
    Something that happened with a system and was reported, by monitoring, by a user or by someone outside, and the assessment of whether it is an incident. An event assessed as an incident is recorded as an AimsIncident.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.8.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records'],
         'mixins': ['AimsRecordMixin'],
         'slot_usage': {'aims_event_type': {'name': 'aims_event_type',
                                            'required': True}}})

    aims_event_type: Literal["AimsSystemEvent"] = Field(default="AimsSystemEvent", description="""The kind of record, AimsSystemEvent or AimsIncident.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsSystemEvent']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_event_occurred_at: Optional[datetime ] = Field(default=None, description="""When the event happened, or when it was first noticed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemEvent']} })
    aims_event_reporter: Optional[str] = Field(default=None, description="""Who reported the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemEvent']} })
    aims_event_source: Optional[str] = Field(default=None, description="""How the event came to light, such as a log, monitoring or a report from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemEvent']} })
    aims_event_adverse_impact: Optional[str] = Field(default=None, description="""The harm that was reported, if any.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.8.3'}},
         'domain_of': ['AimsSystemEvent']} })
    aims_event_assessment: Optional[str] = Field(default=None, description="""What the assessment of the event found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemEvent']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsIncident(AimsSystemEvent):
    """
    An event assessed as an incident: what it concerns, how severe it is, what was done, who was told, and what was learned.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.8.4'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records']})

    aims_incident_category: Optional[AimsIncidentCategory] = Field(default=None, description="""What the incident concerns.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.4'}},
         'domain_of': ['AimsIncident']} })
    aims_incident_threats: Optional[list[AimsAiThreat]] = Field(default=None, description="""The threats peculiar to AI that the incident involved.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_incident_severity: Optional[AimsRiskLevel] = Field(default=None, description="""How severe the incident is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_incident_impact_areas: Optional[list[AimsImpactArea]] = Field(default=None, description="""The areas of impact the incident touched.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_incident_detection_method: Optional[str] = Field(default=None, description="""How the incident was detected.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_incident_response_actions: Optional[list[str]] = Field(default=None, description="""What was done in response.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_incident_recovery_actions: Optional[list[str]] = Field(default=None, description="""What was done to restore normal operation.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_incident_root_cause: Optional[str] = Field(default=None, description="""What caused the incident.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_incident_lessons_learned: Optional[list[str]] = Field(default=None, description="""What the organization learned from it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_incident_notification_required: Optional[bool] = Field(default=None, description="""Whether users, authorities or others had to be told.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.8.4'}},
         'domain_of': ['AimsIncident']} })
    aims_incident_notifications: Optional[list[str]] = Field(default=None, description="""Whom the organization told, and when.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.8.4'}},
         'domain_of': ['AimsIncident']} })
    aims_incident_corrective_actions: Optional[list[str]] = Field(default=None, description="""The corrective actions the incident led to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_incident_closed_at: Optional[datetime ] = Field(default=None, description="""When the incident was closed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsIncident']} })
    aims_event_type: Literal["AimsIncident"] = Field(default="AimsIncident", description="""The kind of record, AimsSystemEvent or AimsIncident.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['AimsSystemEvent']} })
    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_event_occurred_at: Optional[datetime ] = Field(default=None, description="""When the event happened, or when it was first noticed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemEvent']} })
    aims_event_reporter: Optional[str] = Field(default=None, description="""Who reported the event.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemEvent']} })
    aims_event_source: Optional[str] = Field(default=None, description="""How the event came to light, such as a log, monitoring or a report from outside.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemEvent']} })
    aims_event_adverse_impact: Optional[str] = Field(default=None, description="""The harm that was reported, if any.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.8.3'}},
         'domain_of': ['AimsSystemEvent']} })
    aims_event_assessment: Optional[str] = Field(default=None, description="""What the assessment of the event found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsSystemEvent']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsConcernReportingProcess(AimsDocumentControlMixin, AimsRecordMixin):
    """
    The way people raise worries about the organization's part in a system: how it keeps them safe, who looks into a worry, and how fast it answers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.3.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records', 'aims_documented_information'],
         'mixins': ['AimsRecordMixin', 'AimsDocumentControlMixin']})

    aims_concern_process_confidentiality: Optional[list[str]] = Field(default=None, description="""The ways a person can stay unnamed or keep a report private.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.3.3'}},
         'domain_of': ['AimsConcernReportingProcess']} })
    aims_concern_process_audience: Optional[str] = Field(default=None, description="""How staff and contractors learn of it and reach it.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.3.3'}},
         'domain_of': ['AimsConcernReportingProcess']} })
    aims_concern_process_investigators: Optional[str] = Field(default=None, description="""Who looks into a report, and what powers they hold.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.3.3'}},
         'domain_of': ['AimsConcernReportingProcess']} })
    aims_concern_process_escalation: Optional[str] = Field(default=None, description="""How a report reaches management in good time.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.3.3'}},
         'domain_of': ['AimsConcernReportingProcess']} })
    aims_concern_process_reprisal_protection: Optional[str] = Field(default=None, description="""How those who report or investigate are shielded from reprisal.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.3.3'}},
         'domain_of': ['AimsConcernReportingProcess']} })
    aims_concern_process_response_time: Optional[str] = Field(default=None, description="""How soon a report is answered.""", json_schema_extra = { "linkml_meta": {'annotations': {'annex_b_item': {'tag': 'annex_b_item', 'value': 'B.3.3'}},
         'domain_of': ['AimsConcernReportingProcess']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })
    aims_document_reference: Optional[str] = Field(default=None, description="""The reference the organization's document control gives it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_version: Optional[str] = Field(default=None, description="""The version of the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_author: Optional[str] = Field(default=None, description="""Who wrote the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_owner: Optional[str] = Field(default=None, description="""Who answers for the document's content and upkeep.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_format: Optional[str] = Field(default=None, description="""The document's format, such as its language or software version.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_medium: Optional[str] = Field(default=None, description="""What the document is held on, such as paper or an electronic system.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approver: Optional[str] = Field(default=None, description="""Who approved the document.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_approval_date: Optional[date] = Field(default=None, description="""When the document was approved.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_effective_date: Optional[date] = Field(default=None, description="""When the document takes effect.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_last_review_date: Optional[date] = Field(default=None, description="""When the document was last reviewed.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.2'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_next_review_date: Optional[date] = Field(default=None, description="""When the document is next due for review.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_status: Optional[str] = Field(default=None, description="""Where the document stands in its life, in the organization's own terms, such as draft, approved or withdrawn.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_classification: Optional[str] = Field(default=None, description="""The information classification the document carries.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_retention: Optional[str] = Field(default=None, description="""How long the document is kept, as an ISO 8601 duration.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_disposition: Optional[str] = Field(default=None, description="""What becomes of the document when that time is up.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_distribution: Optional[list[str]] = Field(default=None, description="""Who gets the document, how they reach it and what they may do with it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_storage: Optional[str] = Field(default=None, description="""How the document is stored so that it stays legible.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_change_control: Optional[str] = Field(default=None, description="""How changes to the document are controlled, such as version control.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_origin: Optional[bool] = Field(default=None, description="""Whether the document comes from outside the organization and is kept because the system needs it.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })
    aims_document_external_source: Optional[str] = Field(default=None, description="""Who the document came from, when it comes from outside.""", json_schema_extra = { "linkml_meta": {'annotations': {'iso42001_clause': {'tag': 'iso42001_clause',
                                             'value': '7.5.3'}},
         'domain_of': ['AimsDocumentControlMixin']} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


class AimsConcernReport(AimsRecordMixin):
    """
    One worry someone raised about the organization's part in a system, and how it was looked into and settled.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'annotations': {'annex_a_control': {'tag': 'annex_a_control',
                                             'value': 'A.3.3'}},
         'from_schema': 'https://w3id.org/lmodel/iso42001',
         'in_subset': ['aims_ai_system_records'],
         'mixins': ['AimsRecordMixin']})

    aims_ai_systems: Optional[list[str]] = Field(default=None, description="""The AI systems the record concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsPlannedAction',
                       'AimsRiskAssessment',
                       'AimsRisk',
                       'AimsImpactAssessment',
                       'AimsApplicabilityEntry',
                       'AimsControl',
                       'AimsDevelopmentProcess',
                       'AimsResponsibleUseProcess',
                       'AimsTechnicalDocumentation',
                       'AimsUserInformation',
                       'AimsIncidentCommunicationPlan',
                       'AimsReportingObligation',
                       'AimsThirdPartyRelationship',
                       'AimsSystemEvent',
                       'AimsConcernReport']} })
    aims_concern_reported_on: Optional[date] = Field(default=None, description="""When the worry was raised.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_reporter: Optional[str] = Field(default=None, description="""Who raised it, unless they stayed unnamed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_anonymous: Optional[bool] = Field(default=None, description="""Whether the person stayed unnamed.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_channel: Optional[str] = Field(default=None, description="""How it was raised.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_life_cycle_stage: Optional[AimsLifecycleStage] = Field(default=None, description="""The stage of the system's life it concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_severity: Optional[AimsRiskLevel] = Field(default=None, description="""How serious it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_investigator: Optional[str] = Field(default=None, description="""Who looked into it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_investigation_status: Optional[str] = Field(default=None, description="""Where the inquiry stands, in the organization's own terms.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_findings: Optional[str] = Field(default=None, description="""What the inquiry found.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_escalation: Optional[str] = Field(default=None, description="""Whether and how it went up to management.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_response_due: Optional[date] = Field(default=None, description="""When an answer is due.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_responded_on: Optional[date] = Field(default=None, description="""When it was answered.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_resolution: Optional[str] = Field(default=None, description="""How it was settled.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_reprisal_protection: Optional[str] = Field(default=None, description="""What was done to shield those involved from reprisal.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_incidents: Optional[list[str]] = Field(default=None, description="""The incidents it relates to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_concern_nonconformities: Optional[list[str]] = Field(default=None, description="""The nonconformities it relates to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsConcernReport']} })
    aims_id: str = Field(default=..., description="""The record's identifier, unique among the records of the system, such as a URI or a CURIE. Other records refer to the record by it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AimsRecordMixin']} })
    title: str = Field(default=..., description="""The name the organization gives the record.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's title means and carries the same IRI, so "
                      "lokf adapt folds it into LOKF's slot and a knowledge bundle "
                      'reads one title key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the record says or describes, in the organization's own words.""", json_schema_extra = { "linkml_meta": {'comments': ["It means what LOKF's description means and carries the same "
                      "IRI, so lokf adapt folds it into LOKF's slot and a knowledge "
                      'bundle reads one description key.'],
         'domain_of': ['AimsRecordMixin'],
         'slot_uri': 'schema:description'} })

    @field_validator('title')
    def pattern_title(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid title format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid title format: {v}"
            raise ValueError(err_msg)
        return v


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AimsRecordMixin.model_rebuild()
AimsDocumentControlMixin.model_rebuild()
AimsManagementSystem.model_rebuild()
AimsOrganization.model_rebuild()
AimsInterestedParty.model_rebuild()
AimsPolicy.model_rebuild()
AimsTopicSpecificPolicy.model_rebuild()
AimsRole.model_rebuild()
AimsObjective.model_rebuild()
AimsPlannedAction.model_rebuild()
AimsRiskAssessmentProcess.model_rebuild()
AimsRiskAssessment.model_rebuild()
AimsRisk.model_rebuild()
AimsRiskTreatmentProcess.model_rebuild()
AimsRiskTreatmentPlan.model_rebuild()
AimsImpactAssessmentProcess.model_rebuild()
AimsImpactAssessment.model_rebuild()
AimsIdentifiedImpact.model_rebuild()
AimsStatementOfApplicability.model_rebuild()
AimsApplicabilityEntry.model_rebuild()
AimsIncludedControl.model_rebuild()
AimsExcludedControl.model_rebuild()
AimsControl.model_rebuild()
AimsAiSystem.model_rebuild()
AimsSystemResource.model_rebuild()
AimsComponentResource.model_rebuild()
AimsDataResource.model_rebuild()
AimsToolingResource.model_rebuild()
AimsComputingResource.model_rebuild()
AimsHumanResource.model_rebuild()
AimsDevelopmentProcess.model_rebuild()
AimsResponsibleUseProcess.model_rebuild()
AimsTechnicalDocumentation.model_rebuild()
AimsUserInformation.model_rebuild()
AimsIncidentCommunicationPlan.model_rebuild()
AimsReportingObligation.model_rebuild()
AimsResource.model_rebuild()
AimsCompetenceRecord.model_rebuild()
AimsAwarenessProgramme.model_rebuild()
AimsCommunicationPlan.model_rebuild()
AimsCommunication.model_rebuild()
AimsDocumentedInformation.model_rebuild()
AimsOperationalProcedure.model_rebuild()
AimsMonitoringProgramme.model_rebuild()
AimsMonitoringItem.model_rebuild()
AimsAuditProgramme.model_rebuild()
AimsAudit.model_rebuild()
AimsAuditFinding.model_rebuild()
AimsManagementReview.model_rebuild()
AimsNonconformity.model_rebuild()
AimsCorrectiveAction.model_rebuild()
AimsImprovementOpportunity.model_rebuild()
AimsThirdPartyRelationship.model_rebuild()
AimsSupplierRelationship.model_rebuild()
AimsCustomerRelationship.model_rebuild()
AimsSystemEvent.model_rebuild()
AimsIncident.model_rebuild()
AimsConcernReportingProcess.model_rebuild()
AimsConcernReport.model_rebuild()
