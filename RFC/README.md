# NCATS Data Translator (DT) RFC Implementation Process (DRAFT)

-----------
## DT Request for Comment (RFC) Instructions and Guidelines


1. Read the [foundational document to the DT-RFC process](#background).  Your group’s DT-RFC should align with the principles and roles therein.  
2. Create a written draft your DT-RFC as a Google Doc and set the Google Doc Sharing Status as "Anyone with the link can comment"  
	a. The location of the DT-RFC document folder will be provided by DT project management staff  
3. Except for the header, the format of the DT-RFC Google Doc is not prescriptive and should contain content sufficient for the DT-RFC-Type (defined next) and any supporting information or other documents.   The DT-RFC header placed at the beginning of the DT-RFC should contain this information:  
	* DT-RFC-# : {NOTE: Leave blank as this will be assigned by DT-RFC-Governance in Step 4 upon initial submission}  
	* DT-RFC-Title :  
	* DT-RFC-Version : (starting with 1, incremented as required by DT-RFC-Governance in Step 7)  
	* DT-RFC-Type (click the type for definition) :  
		* [Standards](#standards)
		* [Process](#process)
		* [Consensus Building](#consensus-building)
		* [Informational](#informational)
	* Name of the person who is to be Point of Contact for the RFC
	* Email of the person who is to be Point of Contact for the RFC
	* Submitting Group :  
	* Requested RFC posting start date :  
	* Requested RFC posting end date :  
	* Date Emailed for consideration :  
	* DT-RFC-Status : (DT-RFC-Governance will assign an initial value of “Active and open RFC period” updating with values in Steps 6 and 8 as required)
	* URL Link to GitHub : (DT-RFC-Governance will assign a link of where intermediate and final PDFs are stored per Step 9)
	* URL Link to Google Doc : (URL of DT-RFC Google Doc for a given RFC)  

4. Email the RFC Google Doc URL to DT-RFC-Governance at RFCGovernance@dt.groups.io {Christine, Noel, Dena, Stan}.  
	a. Within 1 business day, they will either approve and post to {translator-all@googlegroups.com, translator general slack channel} or email back Point of Contact requesting refinement or clarification  
	b. If posted to {translator-all@googlegroups.com, translator general slack channel}, a unique DT-RFC tag will be assigned based on the pattern: DT-RFC-#  where # is an assigned sequential number.  
5. Once an approved DT-RFC-# posted to {translator-all@googlegroups.com, translator general slack channel}, the Translator community will be proactively encouraged to comment on it during the requested posting period.  
	a. DT project management staff will broadly announce the DT RFC on the start date, halfway through the suggested duration, the day prior, and on the RFC end date.  
	b. Cross-posting by by any NIH DT development participants is encouraged.  
6. Upon conclusion of the DT-RFC-# posting period, the Submitting Group will have ten business days to address comments provided in the DT-RFC-#, assign one of the follow DT-RFC-Status values, and email to DT-RFC-Governance:  
	a. Propose-Resolved  
	b. Propose-Merge (i.e. with another RFC)  
	c. Propose-Postpone  
	d. Propose-Unsuccessful  
	e. Propose-Withdrawn  
7. DT-RFC-Governance will either agree or disagree with the DT-RFC-Status assigned value of the Submitting Group in Step 6:  
	a. If DT-RFC-Governance agrees with the DT-RFC-Status value assigned by the Submitting Group , then the modified DT-RFC-# will be posted for a Final Comment Period (FCP) of no less than 5 business days.  
	b. If DT-RFC-Governance disagrees with the DT-RFC-Status value assigned by the Submitting Group , DT-RFC-Governance will assign a different DT-RFC-Status from the list in Step 6 along with a written explanation and email back to the Point of Contact to restart the DT-RFC process at Step 3 incrementing DT-RFC-Version by 1, or at their discretion, proceed to Step 8 without further iteration.
8. Upon conclusion of the DT-RFC-# Final Comment Period (FCP) or at their discretion, the DT-RFC-Governance will assign one of the following DT-RFC-Status values concluding the DT-RFC process without further iteration:  
	a. Resolved  
	b. Merged (i.e. with another RFC)  
	c. Postponed  
	d. Unsuccessful  
	e. Withdrawn  
9. All versions of of a given DT-RFC Google Doc will be named will be named with Google version history, and an individual PDF of each named version including all contributor comments therein associated with that version will be placed in https://github.com/ResearchSoftwareInstitute/greendatatranslator/rfcs. 







## DT-RFC-Types
#### Standards
A **Standards** Track DT-RFC describes a new feature or implementation for the Translator. It may also describe an interoperability standard that will be supported across the full stacks. Candidate specification must be implemented and tested for correct operation and interoperability by multiple independent parties and utilized in increasingly demanding environments, before it can be adopted as an DT Standard. Candidate specifications should include a description of any external standards that were considered, used, adapted, or rejected.

#### Process
A **Process** DT-RFC describes a process surrounding the Translator, or proposes a change to (or an event in) a process. Process DT-RFCs are like Standards Track DT-RFCs but apply to areas other than the Translator code itself. They may propose an implementation, but not to Translator codebase.  Unlike Informational DT-RFCs, they are more than recommendations, and users are typically not free to ignore them. Examples include procedures, guidelines, and changes to the decision-making process. 

#### Consensus Building
A **Consensus Building** DT-RFC describes a Translator design issue, or provides general guidelines or information to the Translator development community, and may propose a new feature. Unlike Informational DT-RFCs, Consensus Building DT-RFC represent a Translator community consensus or recommendation, so users and implementers are expected to make a best effort to follow their advice.

#### Informational
An **Informational** DT-RFC describes a Translator design issue, or provides general guidelines or information to the Translator development community, but does not propose a new feature. Informational DT-RFCs do not necessarily represent a Translator community consensus or recommendation, so users and implementers are free to ignore Informational DT-RFCs or follow their advice.






## Foundation of the DT-RFC Process
#### Background
The activities of NCATS Data Translator teams play a vital role in the Translator, and are also critical to the Reasoner. In the process of building the Translator we must make decisions, but we need to make decisions based on feedback from individual contributors, the teams, and the many NIH stakeholders, including Translator and Reasoner. Further, there is considerable overlap and interaction between the Translator and the Reasoner, but they have somewhat different responsibilities and timelines. As a result, we need to establish a process that enables effective interactions between the Translator and Reasoner, and also supports shared decision making. To accomplish this, we propose the use of Requests for Comments (RFCs).  

Principles that support the need for RFCs:  
1. Where possible, we enable individual contributors and teams to independently make the decisions necessary to build components, and to subsequently build the Translator.  
2. We actively seek feedback from a broad community of domain experts, and not all of those experts are part of the teams building the Translator or Reasoner.  
3. The teams provide domain expertise and also build communities-of-practice.  
4. The teams help manage the risk in building the Translator.  
5. The teams are responsible for not only providing feedback on the current technology, but also provide context and feedback on future technologies.  
6. The teams will seek input from a broad community of stakeholders outside the DT.  
7. By using RFCs the work of building the Translator can proceed as multiple, interoperable and parallel projects, thus permitting exploration and resiliency.  

The Teams’ roles are:  
1. Each team focuses on challenges that fall within an area of competence that must be addressed for the Translator, and as such they act as community conveners to encourage exploration and innovation.  
2. In cases when challenges and solutions overlap or have dependencies with other teams, a given team will involve other teams and divide the discussions and responsibilities appropriately.  
3. They act as working groups that evaluate key areas of technology necessary for the Translator.  
4. The teams may implement products that are intended to be used by other teams on an ongoing basis.  
5. The teams put forward Requests for RFCs to solicit feedback on key areas in which standards may need to emerge.  

The Reasoner roles are:  
1. Each Reasoner focuses on a set of challenges that must be addressed for a particular aspect of the Translator, as well as the interoperability of the components they build across other Translator components.  
2. The Reasoners act as development teams that implement and evaluate key areas of technology necessary for the Translator.  
3. The Reasoners put forward RFCs to solicit feedback on key areas in which standards may need to emerge.  

An RFC should include participation from all the teams.  
1. The teams provide in-depth technical analysis of possible choices for a given Translator challenge and will implement resources to be used by the Translator where necessary.  
2. The teams serve as the primary implementers of capabilities that are eventually deployed. As such the teams depend on and are informed by the technical analysis done.  
3. Sharing of analyses across the multiple teams allows cross-fertilization of options and approaches.  

Using the RFC process, through consultation with the broader community, allows the teams to:  
1. Initiate or refine potential standards, or  
2. Establish or improve a DT process, or  
3. Build consensus among competing technologies, or  
4. Provide broadly useful information.  

Generally, an RFC should be created when:  
1. We seek to reach agreement.  
2. We seek to establish a contract between actors.  
3. We are defining conventions, e.g., interfaces, APIs, data models, etc.  
4. There is a need for transparency and inclusion on a necessary decision.  
5. A decision could impact more than one system component or team or stakeholders.  
6. We are adding dependencies that can affect more than one team.  


Sources: https://opensource.com/article/17/9/6-lessons-rfcs; https://www.python.org/dev/peps/pep-0001/; https://opensource.com/business/12/6/architecture-participation; https://en.wikipedia.org/wiki/Request_for_Comments; http://aturon.github.io/2018/05/25/listening-part-1/



