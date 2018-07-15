# Proposed DCPPC RFC Implementation Process  
-----------  

The comments and suggestions in this document are being used to stage an RFC for the DCPPC RFC process itself.

### Preamble
The (proposed) DCPPC RFC Process is modeled after industry RFC processes and includes three basic steps: a Google document drafted by and shared with the submitting team/proposer(s) (“Team-DRAFT”), a Google document shared with the DCPPC Consortium for comment and iteration (“DCPPC-DRAFT”), and the final document posted in GitHub for final comment (but not alteration) from the Consortium (“DCPPC-RFC”). We briefly describe when to use each and refer the proposer(s) to the [Sources](#sources) section for elaboration, additional background, or context.  

### Team-DRAFT
The Team-Draft is a document that a team wishing to develop an RFC should create and share within the team. It should be located in place accessible to the entire proposing team, but does not need to made broadly available to the Consortium. The Team-Draft is a document containing preliminary technical specifications, results of related work, or other technical information. Use a Team-Draft to iterate within the proposing team on a design principle, process, guideline, or informational topic before it is polished and before it may be ready to be proposed to the broader DCPPC community for adoption or dissemination. Drafts are intended to be work-in-progress documents for work that may eventually be published as a Request for Comments (RFC). 
When the proposing team has reached consensus on the contents of that draft, the team submits the Team-Draft to the [DCPPC-RFC-Governance](#rfc-governance).  

### DCPPC-DRAFT
After submission, the DCPPC-RFC-Governance creates the DCPPC-DRAFT, which will be promulgated broadly to the Consortium and opened for comment. Using Consortium comments, the proposing team should iterate on the design principle, process, guideline, or informational topic until general consensus is reached. Not all DCPPC-DRAFTs need to become a DCPPC-RFC, nor is it appropriate to refer to an effort as a “Draft RFC” per industry RFC convention. Rather, iterate and refine a DCPPC-DRAFT, and if desired, submit it as a DCPPC-RFC when ready.  

### DCPPC-RFC
The DCPPC-RFC is a publication from the DCPPC community describing a design principle, process, guideline, or information applicable to the working of the NIH Data Commons. It is submitted either for peer review for adherence or adoption by the community or to convey new concepts or information to the community. It is expected that the DCPPC-DRAFT is used as a precursor by a team to refine and polish a design principle, process, guideline, or informational topic and reach general consensus within the Consortium prior to publishing as a DCPPC-RFC. Once published, the text in a DCPPC-RFC will not change per accepted RFC convention.  


|               |Refined, polished?|Content modifiable?|Community-wide?|Require DCPPC RFC Governance to post?|Location|
|---------------|------------------|-------------------|---------------|-------------------------------------|--------|
|**Team-DRAFT** |No                |Yes                |No             |No                                   |Team Google Folder             |
|**DCPPC-DRAFT**|Yes               |Yes                |Yes            |Yes                                  |Google Folder                 |
|**DCPPC-RFC**  |Yes               |No                 |Yes            |Yes                                  |DCPPC GitHub Internal Repo|

Below are the DCPPC-RFC instructions and guidelines. Steps 1-3 are for Team-DRAFT, Steps 4-10 are for the DCPPC-DRAFT preceding the DCPPC-RFC, and steps 11-16 are for the DCPPC-RFC.

-----------

### DCPPC Request for Comments (RFC) Instructions and Guidelines

===
### Team-DRAFT
1. Read the [background document to the DCPPC-RFC process](#background). A Team-DRAFT and eventual DCPPC-DRAFT and DCPPC-RFC should align with the principles and roles therein.  
2. Create, iterate, and refine your Team-DRAFT as a work-in-progress document until the proposing team has reached consensus and is ready to share with the Consortium.  
3. The format of the Team-DRAFT text or the determination of when it is ready to be put forward as a DCPPC-DRAFT is not prescriptive -- your team determines that. The proposing team coordinates the Team-DRAFT content, chooses the scope and audience to iterate it with, chooses when to call it finished, and chooses if/when to submit it as a DCPPC-DRAFT. The DCPPC-RFC-Governance - described in below - is not involved in a Team-DRAFT until or unless it is submitted as a DCPPC-DRAFT.  

### DCPPC-DRAFT
4. Before submission, add the below header to your document. Except for the header, the format of the DCPPC-DRAFT is not prescriptive and should contain content sufficient for the DCPPC-DRAFT-Type (defined next) and any supporting information or other documents.  
The header placed at the beginning of the DCPPC-DRAFT should contain this information:
   * DCPPC-DRAFT-#: (NOTE: Leave blank as this will be assigned by DCPPC-RFC-Governance upon initial submission)   
   * DCPPC-DRAFT-Title:  
   * DCPPC-DRAFT-Type: (click the type for definition):  
    * [Design Principle](#design-principle)
    * [Process](#process)
    * [Consensus Building](#consensus-building)
    * [Informational](#informational)
   * Name of the person who is to be Point of Contact for the DCPPC-DRAFT:  
   * Email of the person who is to be Point of Contact for the DCPPC-DRAFT:  
   * Submitting Team:  
   * Requested DCPPC-DRAFT posting start date:  
   * Date Emailed for consideration:  
   * DCPPC-DRAFT-Status: (DCPPC-RFC-Governance will assign)  
     * Pending  
     * Active and open for comment  

5. Email the DCPPC-DRAFT text to DCPPC-RFC-Governance at RFCGovernance@dcppc.groups.io.  
6. After submission to the DCPPC-RFC-Governance, DCPPC-RFC-Governance project management staff will move the document into a new folder in the shared DCPPC folder and promulgate widely, via email at broadcast@dcppc.groups.io, project-managers@dcppc.groups.io, and the NIH weekly email and via nih-dcppc.slack.com on the general channel and project manager channel (“Distribution List”).  
7. After promulgation to the Consortium, the proposing team should iterate and refine the DCPPC-DRAFT based on Consortium comments. Use the DCPPC-DRAFT to iterate on a design principle, process, guideline, or informational topic until it is polished and ready to be finalized and formally submitted to the Consortium as a DCPPC-RFC.  
8. During the DCPPC-DRAFT process, the proposing team should regularly review the DCPPC-DRAFT and try to resolve issues to develop consensus within the Consortium. However, before clicking “resolve” on any comments, the proposing team should created a saved version of the document, including comments, and save that version as a pdf in the folder for that DCPPC-DRAFT. This will preserve all comments throughout the process to ensure that all community comments are considered. After those comments are addressed, the proposed team should repeat this process after a significant number of additional comments are made.
9.  When the proposing team has determined that the Consortium has no additional substantive comments on the DCPPC-DRAFT, the document can be submitted to the DCPPC-RFC-Governance for conversion to a DCPPC-RFC at the discretion of the proposing team.  
10. Upon conclusion of the DCPPC-RFC posting period, the submitting team will have ten business days to prepare a summary to address comments provided in the DCPPC-RFC. In the summary, agreement and disagreement should be clearly articulated, and proposed decisions to be made, or not made, are clearly articulated. If there are disagreements with the DCPPC-RFC, those disagreements should be clearly articulated in the summary by the authors of the DCPPC-RFC, to the satisfaction of the disagreeing parties (that is, in the summary the articulation of the disagreement is to be to the satisfaction of the disagreeing party, not that the DCPPC-RFC itself is proposed to the satisfaction of all parties).  

### DCPPC-RFC
11. Except for the header, the format of the DCPPC-RFC is not prescriptive and should contain content sufficient for the DCPPC-RFC-Type (defined next) and any supporting information or other documents. The DCPPC-RFC header placed at the beginning of the DCPPC-RFC should contain this information:  
   * DCPPC-RFC-#: (NOTE: Leave blank as this will be assigned by DCPPC-RFC-Governance in Step 4 upon initial submission)  
   * DCPPC-RFC-Title:  
   * DCPPC-RFC-Type: (click the type for definition):  
    * [Design Principle](#design-principle)
    * [Process](#process)
    * [Consensus Building](#consensus-building)
    * [Informational](#informational)
   * Name of the person who is to be Point of Contact for the RFC:  
   * Email of the person who is to be Point of Contact for the RFC:  
   * Submitting Team:  
   * Requested RFC posting start date:  
   * Date Emailed for consideration:  
   * DCPPC-RFC-Status: (DCPPC-RFC-Governance will assign)  
     * Pending  
     * Active and open for comment  
   * URL Link to GitHub : (DCPPC-RFC-Governance will assign a link of where RFC documents are stored)  
12. Email the DCPPC-RFC text to DCPPC-RFC-Governance at RFCGovernance@dcppc.groups.io.  
   a. Within 2 business days, they will either approve or email back the Point of Contact requesting refinement or clarification.  
   b. If approved, the Governance project management team will  
     i. assign a unique DCPPC-RFC tag based on the pattern: DCPPC-RFC-# where # is an assigned sequential number;  
     ii. move the DCPPC-RFC to its GitHub location;  
     iii. update the relevant header information;  
     iv. and post to Distribution Lists.  
13. Once an approved DCPPC-RFC is posted to Distribution Lists, the NIH Data Commons community will be proactively encouraged to comment on it during the requested posting period.  
   a. DCPPC-RFC-Governance project management staff will announce the DCPPC-RFC to Distribution Lists on the start date, halfway through the suggested duration, the day prior, and on the RFC end date.  
   b. Cross-posting by any NIH DCPPC community members is encouraged.  
14. Upon conclusion of the DCPPC-RFC posting period, the submitting team will have ten business days to prepare a summary to address comments provided in the DCPPC-RFC. In the summary, agreement and disagreement should be clearly articulated, and proposed decisions to be made, or not made, are clearly articulated. If there are disagreements with the DCPPC-RFC, those disagreements should be clearly articulated in the summary by the authors of the DCPPC-RFC, to the satisfaction of the disagreeing parties (that is, in the summary the articulation of the disagreement is to be to the satisfaction of the disagreeing party, not that the DCPPC-RFC itself is proposed to the satisfaction of all parties).  
15.  Upon conclusion of the DCPPC-RFC-# posting period or at their discretion, the DCPPC-RFC-Governance will assign one of the following DCPPC-RFC-Status values concluding the DCPPC-RFC process without further iteration:  
   a. Resolved  
   b. Merged (i.e. with another DCPPC-RFC)  
   c. Postponed  
   d. Unsuccessful  
   e. Withdrawn  
16. All documents from a concluded DCPPC-RFC with all contributor comments will be placed in https://github.com/dcppc/internal/rfcs. 


-----------

## DCPPC-RFC-Types
#### DRAFT Consensus Building
A **DRAFT Consensus Building** DCPPC-RFC describes a NIH Data Commons design issue, or provides general guidelines or information to the NIH Data Commons development community, and may propose a new feature. This type of RFC type includes use cases or demonstration of how the design, guideline, or information meets a specific need, and/or which stakeholders' needs have been met. Precursor to DCPPC-RFCs, DRAFT Consensus Building drafts represent a NIH Data Commons community consensus or recommendation, so users and implementers are expected to make a best effort to contribute to the dialogue surrounding the draft.

#### Design Principle
A  **Design Principle** DCPPC-RFC describes a new feature or implementation for the NIH Data Commons. It may also describe an interoperability design principle that will be supported across the full stacks. Candidate specification must be implemented and tested for correct operation and interoperability by multiple independent parties and utilized in increasingly demanding environments, before it can be adopted as an DCPPC Design Principle. Candidate specifications should include a description of any external design principles and/or standards that were considered, used, adapted, or rejected.

#### Process
A **Process** DCPPC-RFC describes a process surrounding the NIH Data Commons, or proposes a change to (or an event in) a process. Process DCPPC-RFCs are like Design Principle DCPPC-RFCs but apply to areas other than the NIH Data Commons code itself. They may propose an implementation, but not to NIH Data Commons codebase.  Unlike Informational DCPPC-RFCs, they are more than recommendations, and users are typically not free to ignore them. Examples include procedures, guidelines, and changes to the decision-making process. 

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


#### Sources  
https://opensource.com/article/17/9/6-lessons-rfcs  
https://en.wikipedia.org/wiki/Internet_Draft  
https://en.wikipedia.org/wiki/Request_for_Comments  
https://www.python.org/dev/peps/pep-0001/  
https://opensource.com/business/12/6/architecture-participation  
http://aturon.github.io/2018/05/25/listening-part-1/  

#### RFC Governance
Titus Brown   
Owen White  
Stan Ahalt  




