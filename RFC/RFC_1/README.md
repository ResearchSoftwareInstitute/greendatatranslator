**DCPPC-RFC-# :** 1   
**DCPPC-RFC-Title :** KC6 Security, Ethics, and Privacy Use Cases  
**DCPPC-RFC-Type :** Consensus Building  
**Name of the person who is to be Point of Contact for the RFC :** Kevin Wilson  
**Email of the person who is to be Point of Contact for the RFC :** kwilson@rti.org  
**Submitting Individual or Group :** KC6  
**Requested RFC posting start date :** 06/25/2018  
**Requested RFC posting end date :** 07/13/2018  
**Date Emailed for consideration :** 06/20/2018  
**DCPPC-RFC-Status :** Pending  
**URL Link to GitHub :**   
**URL Link to this Document :** https://docs.google.com/document/d/1Eizi5W7oV45gmQ-QO3AqXwZOPQdhWGDPX_qecroR3xI/edit  
  
# NIH Data Commons

# KC6 Security, Ethics, and Privacy Use Cases

Prepared by the KC6 Use Cases Working Group:
*Becky Boyles*  
*Moran Cabili*  
*Erin Friday*  
*Ray Idaszak*  
*Juergen Klenk*  
*Cathy Laurie*  
*Alison Leaf*  
*Jessica Lyons*  
*Sarah Nelson*  
*Saiju Pyarajan*  
*Anurag Sethi*  
*Kevin Wilson*  


Version 1.0  
16 June 2018  

Table of Contents  
**Introduction**	4  
**Authentication and Identity Management**	4  
UC-1.	Provision of User Identities in a Full Stack System	4  
UC-2.	Authenticate Using Single Sign-on	4  
UC-3.	Authenticate User with Trusted Identify Provider	5  
UC-4.	Support Multi-level Authentication	5  
UC-5.	Establish Identity Authority	5  
UC-6.	Support a Range of Digital Identities	5  
UC-7.	Authenticate Prior to Deployment of Computational Workspace	5  
UC-8.	Authenticate User to FISMA-Compliant Workspace	6  
UC-9.	Link Identities to Signify Institutional Relationships	6  
UC-10.	Authenticate Through a Full Stack’s Web Portal	6  
UC-11.	Validate Identity	6  
UC-12.	Support Delegation of Signing Authority	6  

Authorization and Data Access	6  
UC-13.	Authorize Data Access According to Dataset Access Requirements	7  
UC-14.	Establish an Authorization Registry	7  
UC-15.	Authorize Data Access According to Different Levels	7  
UC-16.	Access Data Based on Existing DAR	7  
UC-17.	Facilitate Access to User-Submitted Data	7  
UC-18.	Verify Access Permissions when Executing Workflows	8  
UC-19.	Request and Obtain Data Access	8  
UC-20.	Prevent Unauthorized Data Sharing	8  
UC-21.	Prevent Unauthorized Data Use	8  
UC-22.	Provision Compliant Computing Workspace	8  
UC-23.	Apply Institutional Signature to All Relevant Datasets	8  
UC-24.	Preauthorize Access to Data Sets	9  

Auditing and Logging	9
UC-25.	Log Unsuccessful Authentication Attempts	9
UC-26.	Log Dataset Access Requests	9
UC-27.	Log Data Analysis Steps	9
UC-28.	Conduct Risk Assessment and Log the Result	9
UC-29.	View Data Access Summary	10
UC-30.	View Data Access Details	10
UC-31.	View Data Commons Project Activity Log	10
UC-32.	View Data Access and Attribution Log	10
UC-33.	Retrieve List of Resources Accessed	10
UC-34.	Facilitate Security Audit	11
UC-35.	Facilitate Audit of Resource Use	11
UC-36.	View Datasets to which Associated Researchers Have Access	11
UC-37.	Audit Researcher Activities	12
UC-38.	Automate Oversight of Data Use	12
Interoperability	12
UC-39.	Facilitate Cross-Stack Data Access	12
UC-40.	Integrate Data Across Stacks	12
UC-41.	Support Interoperability of APIs	12
UC-42.	Mirror Authorization Across All Commons Tools	13
UC-43.	Identify Datasets	13



Introduction

This document contains a series of use cases, which serve to inform the Security, Ethics, and Privacy-related functionality that needs to be incorporated into the NIH Data Commons full stack systems. Each user story identifies a key use case along with a recommendation for whether the functionality should be incorporated into the systems within the 180-day pilot phase of the project or whether it is a longer-term activity. The purpose of this document is to facilitate communication and consensus around Security, Ethics, and Privacy-related functionality and once approved, it will serve as a roadmap for policy and technical implementation.
Each use case is described in terms of a user story. The use cases incorporate the perspective of a range of data commons stakeholders, with each user representing a specific set of stakeholders. Featured users are:
Maria – data commons end user;
Alice – proprietor of a full stack;
Bruce – principal investigator (PI);
Jane – compliance officer;
Claire – study PI;
Jennifer – study participant;
Joe – data provider;
Sarah – governance.
The use cases that follow are designed to inform technical and policy requirements and, as such, do not address implementation details. Each full stack team will determine how the finalized use cases should be implemented.
Authentication and Identity Management

Provision of User Identities in a Full Stack System
Maria provides proof of identity​ to the authentication authority. The identity authority updates their registry such that the API will verify Maria's identity. The full stack provisions user identities for Maria in their data platform and in their compute platforms.

Timing: Pilot

Authenticate Using Single Sign-on 
Maria authenticates to one of the Full Stacks using her credentials. She should be required to authenticate only once within a single computing session. Once she has authenticated, she should be able to access (assuming they meet the necessary authorization criteria) resources across all data commons stacks.

Timing: Pilot


Authenticate User with Trusted Identify Provider
Maria would like to authenticate to one of the full stacks. When she authenticates, the authentication application should review the identity information returned and determine whether or not it satisfies a specific set of criteria. If it doesn’t, the user must be guided through the process of satisfying the criteria through further authentication actions. The criteria for acceptable identification ensures that the user must have authenticated his or her identity using one of a set of trusted identity providers and that the authentication must have occurred not more than X seconds/minutes/hours ago.

Timing: Pilot 

Support Multi-level Authentication
Maria initially logs in to a full stack using single-factor authentication. When Maria tries to access a dataset, the system determines that additional authentication requirements must be met, such as two-factor authentication. In this case, the system must guide Maria through the process of meeting these additional requirements.

Timing: Post-pilot

Establish Identity Authority
Alice, as one of the proprietors of the full stack selects a legally and technologically appropriate entity to manage user identities. The identity authority implements an authentication protocol and technology stack to include: encryption protocols and requirements, a secure, well documented, and a reliable web API. The identity authority implements and publishes credential criteria and protocols (two factor, dongle, etc.).

Timing: Pilot

Support a Range of Digital Identities
As a data commons user, Maria would like to be able to authenticate using eRA Commons, Google Identity, AWS identity or her Institutional Identity.

Timing: Pilot

Authenticate Prior to Deployment of Computational Workspace
Maria authenticates through a full stack’s web portal, launches a Jupyter notebook in a workspace for computation, and connects to a data analytic service (e.g., Spark). The workspace for computation transmits Maria’s token in the request to the data analytic service. The data analytic service invokes KAS to validate or reject Maria’s authentication token. If authenticated, virtual infrastructure is deployed and configured to use authentication token provided for Maria hence having access to other resources to which Maria has access to such as data grid. A billing infrastructure audits Maria's resource consumption.

Timing: Pilot

Authenticate User to FISMA-Compliant Workspace
Having authenticated to a full stack, Maria requests a FISMA-compliant VM in the cloud for a workspace for working with sensitive data. The web portal transacts multi-factor authentication to instantiate a FISMA-moderate workspace. Embedded technical security policies (i.e., Data Tags) are enacted as first-class citizens within metadata to support the data-driven security controls.  An audit trail commences to track when data comes in or out, who’s accessing data, when they accessed it, and when it moves, and who moves it. Automatic generation of event logs based on FISMA controls are made available.

Timing: Post-pilot

Link Identities to Signify Institutional Relationships
As PI, Bruce would like to easily specify the members of his team and their electronic identities, and have these identities linked to his own identity in a manner that signifies the PI-Researcher relationship.

Timing: Post-pilot

Authenticate Through a Full Stack’s Web Portal
Maria attempts to directly access content on the full stack’s web portal requiring authentication. If Maria is denied access, she is notified of the result of the authentication attempt but not the reasons.

Timing: Pilot

Validate Identity
As Compliance Officer, Jane would like the Data Commons System to feature “identity-proofing” so that a researcher’s physical identity is linked to their electronic identity, allowing her to identify and remediate researchers that break guidelines.

Timing: Post-pilot

Support Delegation of Signing Authority
As PI, Bruce would like to have the ability to delegate to his admin or project manager the ability to edit (but not submit) his data access requests and manage access to his team members.

Timing: Post-pilot
Authorization and Data Access

Authorize Data Access According to Dataset Access Requirements
After authenticating, Maria attempts to access a dataset. Regardless of which service authenticates Maria, the system should automatically determine whether she meets the criteria to gain access to the dataset. The system must ensure that Maria meets all necessary conditions. For example, if formal IRB approval is required then there must be a mechanism for the service to verify that this approval has been obtained. If Maria has appropriate permissions she should be afforded access to the dataset. If she does not have appropriate permissions, the system should deny her access to the dataset.

Timing: Post-pilot

Establish an Authorization Registry
Alice, a proprietor of a full stack selects a legally and technologically appropriate entity to manage data access entitlements. The authorization registry develops and publishes a taxonomy of entitlements representing levels of capability.

Timing: Post-pilot

Authorize Data Access According to Different Levels
Maria enters agreements and contracts entitling her to access data sets at various levels. The authorization registry records Maria's entitlements in an authorization data store. The authorization registry expresses facts about all of Maria's agreements and contracts in the taxonomy's schema. The authorization registry is used in the future to determine which datasets Maria has access to and what permissions she has.

Timing: Post-pilot

Access Data Based on Existing DAR
As a study PI, Claire would like to access data in the Commons for which she already has an approved dbGaP DAR, without having to re-apply for access.

Timing: Pilot
 
Facilitate Access to User-Submitted Data
Maria would like to publish a dataset in the commons. She is required to provide evidence of data sharing agreements in order to publish the data in the commons. If Alice wants to access this dataset, she must “sign” the data sharing agreement in order to access the data.

Timing: Post-pilot


Verify Access Permissions when Executing Workflows
Maria makes a successful authentication attempt to the full stack’s portal application and then selects a workspace for her Spark or CWL workflow to execute. Maria's computation attempts to access a file in the data grid (e.g., TOPMed, GTEx, etc.). Access control configuration within the data grid consults Maria's credential to validate her access. The data grid grants or denies access based on access control metadata associated with the valid token.

Timing: Post-pilot

Request and Obtain Data Access
Maria would like to be able to request data access through the Data Commons System and wait no more than one day between applying for access to a dataset and being granted access to it.

Timing: Post-pilot

Prevent Unauthorized Data Sharing
As PI, Bruce would like the Data Commons System to that ensure that members of his team are not able to unintentionally redistribute data using Commons services to researchers that are not authorized to see them.

Timing: Pilot

Prevent Unauthorized Data Use
As PI, Bruce would like the Data Commons System to ensure that it is not possible to unintentionally violate data use restrictions when his team are using Commons Services.  For example, he would like to ensure that none of his team members ever put “cancer only” and “diabetes only” datasets in the same workspace and do a joint analysis on them to study cancer.

Timing: Post-pilot

Provision Compliant Computing Workspace
Maria authenticates to a full stack and requests access to a dataset and a workspace to conduct an analysis. The system must ensure that the computing environment provided to the Maria meets all regulatory, security, and privacy requirements of the dataset. For example, if a given dataset requires a FISMA moderate environment, then this environment should be the instantiated be the means through which the dataset is accessed.

Timing: Post-pilot

Apply Institutional Signature to All Relevant Datasets
Once approved for a dataset from an institution, Maria would like to not have to get re-approved by the signing official at her Institution for each dataset she applies for access to.

Timing: Post-pilot

Preauthorize Access to Data Sets
As Signing Official, Marion would like to be able to pre-authorize researchers at her institution to access Commons datasets, rather than having to re-sign for each request to access data.

Timing: Post-pilot
Auditing and Logging

Log Unsuccessful Authentication Attempts
Alice, a user of the NIH Data Commons Pilot Phase Consortium (DCPPC) system (the “System”), logs in to the System using the credentials she previously applied and approved from an authentication provider (the “Authenticator”), which is tightly integrated with the System. She forgets her password, so only successfully logs in at the second attempt. The Authenticator collects details about these log-in activities, whether successful or not, and logs them in an audit trail.

Timing: Pilot

Log Dataset Access Requests
After logging in, Alice can see the datasets and resources that are available in the System.  Access to these resources are controlled by an authorization provider (the “Authorizer”). Alice chooses a dataset and submits an access request.  The Authorizer collects details about her request and logs the data access request. 

Timing: Pilot

Log Data Analysis Steps
Alice requests to perform a specific analysis on a specific dataset using a workflow that is managed by the System. Access is granted by the authorizer, and the request details are logged.  The analysis is conducted using a third-party DCPPC component and the steps in the analysis are logged. 

Timing: Pilot

Conduct Risk Assessment and Log the Result
Alice performs certain type of data analysis (e.g., count query) that has been flagged within the System as requiring a risk assessment to be performed for every access request.  The system performs the necessary risk evaluation/assessment and logs the result.

Timing: Post-pilot

View Data Access Summary
As a participant in a study, Jennifer would like to be able to see a summary of how many users and/or analysis projects have utilized data from the study in which she is a participant. Ideally, she could do this from a publicly-accessible view, i.e. without having to log into the Commons or otherwise verify/assert her identity as a participant in a given study (which would have the danger of exposing her identity, in addition to being very difficult to assert).

Timing: Post-pilot

View Data Access Details
As a study PI, Claire would like to be able to see information about the users who have been granted access to her study’s data in the Commons. If possible, this information should include the user name and institutional affiliation. She should also be able to see information about frequency and volume of analyses run on her study’s data in the Commons.

Timing: Post-pilot

View Data Commons Project Activity Log
Alice is preparing a periodic report of activity on a project.  She has performed a significant portion of work for the project on the NIH Data Commons.  She accesses the Data Commons user interface for querying the project activity log.  The user interface allows her to specify her search criteria which include her system UID and the start date and end date of the time window she’s interested in. The data returned contains all relevant of the activity on the project but may not contain certain data elements that are used by the system for its internal processing.

Timing: Post-pilot

View Data Access and Attribution Log
Joe, the provider of a resource on the Data Commons, is preparing a report documenting how frequently his resource is being used by consumers in the community.  He would like to know if his resource is properly credited/acknowledged. In addition to his own, internal logs, he wants to query the system to get a list of activity originating in the Data Commons.  He accesses the Data Commons user interface for querying the data access log.  The user interface allows him to specify his search criteria, which include the UID of his resource(s) within the Data Commons and the start date and end date of the time window he’s interested in.  The process returns all logged activity for the specified resources during the specified time window. 

Timing: Post-pilot 

Retrieve List of Resources Accessed
Alice is preparing a paper for publication on a project she is completing.  She has performed a significant portion of work for the project on the NIH Data Commons.  She wants to prepare a list of Data Commons resources to include in the references section of the publication.  She accesses the Data Commons user interface for querying the Distributed Ledger.  The user interface allows her to specify her search criteria which include her system UID, the start date and end date of the time window, and the GUID for the resource she’s interested in.  The process returns a block of data containing an accounting of each all logged activity for the specified user during the specified time window, related to the specified resource.  The data returned contains all relevant details from the ledger but may not contain certain data elements that are used by the System for its internal processing.

Timing: Post-pilot

Facilitate Security Audit
Sarah, who represents a Governance Authority (the Authority), is performing a security audit on a resource in the Data Commons.  She accesses the Data Commons user interface for querying the audit trail.  The user interface allows her to specify her search criteria, potentially including an assertion that her query is being made with elevated permissions, for system security purposes.  Her search criteria include the GUID of resource, as well as the start date and end date of the time window of interest.  The data returned contains all relevant details from the ledger including the UIDs of the users who performed each activity and any updating entries to the activity records in the audit trail that contain risk assessment scores for particular activities.  The data returned may not contain certain data elements that are used by the system for its internal processing.

Timing: Post-pilot

Facilitate Audit of Resource Use
Sarah, who represents a Governance Authority, is performing an audit on a resource in the Data Commons to determine equitable use/attribution.  She accesses the Data Commons user interface for querying the audit trail.  The user interface allows her to specify her search criteria, potentially including an assertion that her query is being made with elevated permissions, for System equity analysis purposes.  Her search criteria include the GUID of the resource, as well as the start date and end date of the time window of interest (other search criteria of interest may be determined by the KC1 working group, during the pilot phase).  The data returned contains all relevant details from the audit trail including the UIDs of the users who performed each activity and any additional data elements, or references to linked resources, that are deemed relevant to an analysis of equity of use/attribution.  The data returned may not contain certain data elements that are used by the system for its internal processing.

Timing: Post-pilot

View Datasets to which Associated Researchers Have Access 
As PI, Bruce would like to have access to updated information on what members of his team have access to which datasets.

Timing: Post-pilot

Audit Researcher Activities
As Compliance Officer, Jane would like to be able to easily audit researchers and inspect their workspace so that she can see documentation of their stated research purpose, proof of IRB approval (if required), and determine that their stated research purpose agrees with the work that was actually done.

Timing: Post-pilot

Automate Oversight of Data Use
As a member of the Data Access Committee, Sarah would like the Data Commons System to support computer-assisted data use oversight, meaning that the data use restrictions for each dataset are expressed in machine-readable standard form (i.e., expressed using a standardized ontology), there is a machine-readable standard statement of research purpose accompanying each (human-readable application for access to data), and an algorithm compares the data use restrictions to the researcher’s purpose and lets her know whether the two are compatible and if manual review is required.

Timing: Post-pilot
Interoperability

Facilitate Cross-Stack Data Access
Maria authenticates to one full stack and would like to access a dataset on a second full stack. The second full stack consults a common authorization service to determine Maria's access entitlements and allows or denies access to the file or service as appropriate.

Timing: Post-pilot

Integrate Data Across Stacks
Maria would like to access data stored on one full stack through the data grid on a second full stack. To access these data, she uses the DOS API. The first full stack’s KAS uses an opaque identity token which allows retrieval of a token from the second full stack. The first full stack’s data grid consults KAS using identity token to retrieve second full stack’s access token. The first full stack. allows or declines data access based on the second full stack’s policies.

Timing: Post-pilot

Support Interoperability of APIs
In the course of using the Data Commons System, Maria requires the use of multiple APIs across different service providers. The application (web site, desktop program, etc.) should use generic (third-party) code to obtain the authorization tokens necessary to use REST APIs provided by multiple service providers. The application must use authorized REST APIs from at least two independent (unaffiliated) service providers. Multiple REST APIs secured by a service provider may be used, in addition to the minimum two. Both service providers should provide OAuth2-based authorization for their APIs. The application’s registration process with respect to the service providers must be documented. The application must use the same standard (generic, third-party) OAuth2 code when gaining access to each API. The application must display the end-user identity information that was returned from each service provider. The application must display the results of accessing the REST API from each service provider. The application should perform some integrated operation between the REST APIs, such as retrieving data from one and computing on it via another. 

Timing: Post-pilot

Mirror Authorization Across All Commons Tools
Jennifer would like to apply for access to data and, if she is granted permission to use it, have this authorization mirrored across all Commons tools without having to re-apply for access.

Timing: Post-pilot

Identify Datasets
Maria would like to be able to state her research purpose using a standard format that ideally will not require/minimize typing free text, and have the system automatically identify all datasets whose data use restrictions are consistent with her research purpose.

Timing: Post-pilot








