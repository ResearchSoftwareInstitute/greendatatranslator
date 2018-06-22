# DCPPC-DRAFT  
## Proposed DCPPC RFC Implementation Process  
-----------

The comments and suggestions in this document are being used to stage an RFC for the DCPPC RFC process itself.  

### Preamble
The (proposed) DCPPC RFC Process is modeled after industry RFC processes and includes two basic steps: a DCPPC-DRAFT and the actual DCPPC-RFC.  We briefly describe when to use each and refer the proposer(s) to the Sources section   for elaboration, additional background, or context.

### DCPPC-DRAFT
The DCPPC-DRAFT is a document containing preliminary technical specifications, results of related work, or other technical information.  Drafts are intended to be work-in-progress documents for work that may eventually be published as a Request for Comments (RFC).  Use a DCPPC-DRAFT to iterate on a design principle, process, guideline, or informational topic before it is polished and before it may be ready to be proposed to the broader DCPPC community for adoption or dissemination.  Not all DCPPC-DRAFTs need to become a DCPPC-RFC, nor is it appropriate to refer to an effort as a “Draft RFC” according to industry RFC convention. Rather, iterate and refine a DCPPC-DRAFT, and if desired, submit it as a DCPPC-RFC when ready.

### DCPPC-RFC
The DCPPC-RFC is a publication from the DCPPC community describing a design principle, process, guideline, or information applicable to the working of the NIH Data Commons. It is submitted either for peer review for adherence or adoption by the community, or to convey new concepts or information to the community.  It is expected that the DCPPC-DRAFT is used as a precursor by an individual or group to refine and polish a design principle, process, guideline, or informational topic prior to publishing as a DCPPC-RFC.  As a publication, the text in a published DCPPC-RFC will not change once published according to accepted RFC convention.



|               |Refined, polished?|Content modifiable?|Community-wide?|Require DCPPC RFC Governance to post?|
|---------------|------------------|-------------------|---------------|-------------------------------------|
|**DCPPC-DRAFT**|No                |Yes                |Not necessarily|No                                   |
|**DCPPC-RFC**  |Yes               |No                 |Yes            |Yes                                  |


Below are the DCPPC-RFC instructions and guidelines.  Steps 1 and 2 are for the DCPPC-DRAFT preceding the DCPPC-RFC, and steps 3-8 are for the DCPPC-RFC.

-----------


### DCPPC Request for Comments (RFC) Instructions and Guidelines

===
### DCPPC-DRAFT
1. Read the [background document to the DCPPC-RFC process](#background).  Your individual or group’s DCPPC-DRAFT and eventual DCPPC-RFC should align with the principles and roles therein.
2. Create, iterate, and refine your DCPPC-DRAFT as a work-in-progress document for work you or your group may be positioning to be published as a DCPPC-RFC, when ready, as a Request for Comments (RFC).  Use your DCPPC-DRAFT to iterate on a design principle, process, guideline, or informational topic until it is polished and ready to be proposed to the broader DCPPC community for adoption or dissemination.  The format of the DCPPC-DRAFT text or determining when it is ready to be put forward as a DCPPC-RFC is not prescriptive - you or your group determine that. The proposing individual or group coordinates the DCPPC-DRAFT content, chooses the scope and audience to iterate it with, chooses when to call it finished, and chooses if/when to submit it as a DCPPC-RFC.  The DCPPC-RFC-Governance - described in Step 4 below - is not involved in a DCPPC-DRAFT until or unless it is submitted as a DCPPC-RFC.

===
### DCPPC-RFC
3. Except for the header, the format of the DCPPC-RFC is not prescriptive and should contain content sufficient for the DCPPC-RFC-Type (defined next) and any supporting information or other documents.   The DCPPC-RFC header placed at the beginning of the DCPPC-RFC should contain this information:
  * DCPPC-RFC-# : (NOTE: Leave blank as this will be assigned by DCPPC-RFC-Governance in Step 4 upon initial submission)
  * DCPPC-RFC-Title : 
  * DCPPC-RFC-Type : (click the type for definition):
    * [Design Principle](#design-principle)
    * [Process](#process)
    * [Consensus Building](#consensus-building)
    * [Informational](#informational)
  * Name of the person who is to be Point of Contact for the RFC : 
  * Email of the person who is to be Point of Contact for the RFC : 
  * Submitting Individual or Group : 
  * Requested RFC posting start date : 
  * Requested RFC posting end date : 
  * Date Emailed for consideration : 
  * DCPPC-RFC-Status : (DCPPC-RFC-Governance will assign)
    * Pending
    * Active and open for comment
  * URL Link to GitHub : (DCPPC-RFC-Governance will assign a link of where RFC documents are stored per Step 8)
  * URL Link to RFC Text (URL of DCPPC-RFC text for a given RFC)

4. Email  the DCPPC-RFC text to DCPPC-RFC-Governance at RFCGovernance@dcppc.groups.io {Owen, Titus, Stan}
  a. Within 2 business days, they will either approve and post to {leads@dcppc.groups.io, nih-dcppc general slack channel} or email back Point of Contact requesting refinement or clarification.
  b. If posted to {leads@dcppc.groups.io, nih-dcppc general slack channel}, a unique DCPPC-RFC tag will be assigned based on the pattern: 
DCPPC-RFC-#  where # is an assigned sequential number 

5. Once an approved DCPPC-RFC-# is posted to {leads@dcppc.groups.io, nih-dcppc general slack channel}, the NIH Data Commons community will be proactively encouraged to comment on it during the requested posting period.
  a. DCPPC project management staff will broadly announce the DCPPC RFC on the start date, halfway through the suggested duration, the day prior, and on the RFC end date.
  b. Cross-posting by any NIH DCPPC community members is encouraged.

6. Upon conclusion of the DCPPC-RFC-# posting period, the Submitting Individual or Group will have ten business days to prepare a summary to address comments provided in the DCPPC-RFC-#. In the summary, agreement and disagreement should be clearly articulated, and proposed decisions to be made, or not made, are clearly articulated. If there are disagreements with the RFC, those disagreements should be clearly articulated in the summary by the authors of the RFC, to the satisfaction of the disagreeing parties (that is, in the summary the articulation of the disagreement is to be to the satisfaction of the disagreeing party, not that the RFC itself is proposed to the satisfaction of all parties).

7. Upon conclusion of the DCPPC-RFC-# posting period or at their discretion, the DCPPC-RFC-Governance will assign one of the following DCPPC-RFC-Status values concluding the DCPPC-RFC process without further iteration:
  a. Resolved
  b. Merged (i.e. with another DCPPC-RFC)
  c. Postponed
  d. Unsuccessful
  e. Withdrawn

8. All documents from a concluded DCPPC-RFC with all contributor comments will be placed in https://github.com/dcppc/internal/rfcs. 


-----------




## DCPPC-RFC-Types
#### Design Princples
A  **Design Principle** DCPPC-RFC describes a new feature or implementation for the NIH Data Commons. It may also describe an interoperability design principle that will be supported across the full stacks. Candidate specification must be implemented and tested for correct operation and interoperability by multiple independent parties and utilized in increasingly demanding environments, before it can be adopted as an DCPPC Design Principle. Candidate specifications should include a description of any external design principles and/or standards that were considered, used, adapted, or rejected.

#### Process
A **Process** DCPPC-RFC describes a process surrounding the NIH Data Commons, or proposes a change to (or an event in) a process. Process DCPPC-RFCs are like Design Principle DCPPC-RFCs but apply to areas other than the NIH Data Commons code itself. They may propose an implementation, but not to NIH Data Commons codebase.  Unlike Informational DCPPC-RFCs, they are more than recommendations, and users are typically not free to ignore them. Examples include procedures, guidelines, and changes to the decision-making process. 

#### Consensus Building
A **Consensus Building** DCPPC-RFC describes a NIH Data Commons design issue, or provides general guidelines or information to the NIH Data Commons development community, and may propose a new feature. This type of RFC type includes use cases or demonstration of how the design, guideline, or information meets a specific need, and/or which stakeholders' needs have been met. Unlike Informational DCPPC-RFCs, Consensus Building DCPPC-RFC represent a NIH Data Commons community consensus or recommendation, so users and implementers are expected to make a best effort to follow their advice.

#### Informational
An Informational DCPPC-RFC describes a NIH Data Commons design issue, or provides general guidelines or information to the NIH Data Commons development community, but does not propose a new feature. Informational DCPPC-RFCs do not necessarily represent a NIH Data Commons community consensus or recommendation, so users and implementers are free to ignore Informational DCPPC-RFCs or follow their advice.





## Foundation of the DCPPC-RFC Process
#### Background
The activities of both the Full Stacks (FSs) and the Key Capabilities (KCs) play a vital role in the Data Commons (DC), and are also critical to the NHLBI Data STAGE. In the process of building the Data Commons we must make decisions, but we need to make decisions based on feedback from individual contributors, the FSs, the KCs, and the many NIH stakeholders, including Data STAGE.  Further, there is considerable overlap and interaction between the KCs and the FSs, but they have somewhat different responsibilities and timelines.  As a result, we need to establish a process that enables effective interactions between the KCs and the FSs, and also supports shared decision making.  To accomplish this, we propose the use of Requests for Comments (RFCs).

Principles that support the need for RFCs:
1. Where possible, we enable individual contributors and teams to independently make the decisions necessary to build components, to build the FSs, and to subsequently build the DC.
2. We actively seek feedback from a broad community of domain experts, and not all of those experts are part of the teams building the KCs, the FSs, the DC, or STAGE.
3. The KCs provide domain expertise and also build communities-of-practice.
4. The KCs help the DC to manage the risk in building the DC.
5. The KCs are responsible for not only providing feedback on the current technology, but also provide context and feedback on future technologies.
The KCs operate asynchronously from the FSs.
6. The FSs will seek input from a broad community of stakeholders outside the DCPPC.
7. By using RFCs the work of building the DC can proceed as multiple, interoperable and  parallel projects, thus permitting exploration and resiliency.

The KCs’ roles are:
1. Each KC focuses on challenges that fall within an area of competence that must be addressed for the DC, and as such they act as community conveners to encourage exploration and innovation.
2. In cases when challenges and solutions overlap or have dependencies with other KCs, the KC will involve other KCs and divide the discussions and responsibilities appropriately. 
3. They act as working groups that evaluate key areas of technology necessary for the Data Commons (DC).
4. The KCs may implement products that are  intended to be used by the FSs on an ongoing basis.
5. The KCs put forward Requests for RFCs to solicit feedback on key areas in which standards may need to emerge.

The FSs’ roles are:
1. Each FS focuses on a set of challenges that must be addressed for a particular implementation of the DC, as well as the interoperability of the components they build across other stacks.
2. The FSs act as development teams that implement and evaluate key areas of technology necessary for the Data Commons.
3. The FSs put forward RFCs to solicit feedback on key areas in which standards may need to emerge.

An RFC should include participation from all the FS teams. Interaction between KCs and FSs
1. The KCs serve as the group that provides in-depth technical analysis of possible choices for a given DC challenge and will implement resources to be used by the FS where necessary.
2. The FSs serve as the primary implementers of capabilities that are eventually deployed. As such the FSs depend on and are informed by the technical analysis done the KCs.
3. Sharing of KC analyses across the multiple teams allows cross-fertilization of options and approaches across the FSs.

Using the RFC process, through consultation with the broader community, allows the KCs and the FSs to:
1. Initiate or refine potential community standards as design principles, or 
2. Establish or improve a DCPPC process, or
3. Build consensus among competing technologies, or
4. Provide broadly useful information.

Generally, an RFC should be created when:
1. We seek to reach agreement.
2. We seek to establish a contract between actors.
3. We are defining conventions, e.g.,  interfaces, APIs, data models, etc.
4. There is a need for transparency and inclusion on a necessary decision.
5. A decision could impact more than one system component or team or stakeholders.
6. We are adding dependencies that can affect more than one team.


Sources: 
https://opensource.com/article/17/9/6-lessons-rfcs
https://en.wikipedia.org/wiki/Internet_Draft
https://en.wikipedia.org/wiki/Request_for_Comments 
https://www.python.org/dev/peps/pep-0001/
https://opensource.com/business/12/6/architecture-participation
http://aturon.github.io/2018/05/25/listening-part-1/






