Project Earthquake
===
The following project has been created to apply to the position: Data Engineer, at Pleo.

# Deliverables
- [x] Deployable in production
- [x] Tests have been added
- [ ] Scheduled query that should run once a week
- [x] Explanation of how to run the service and test it
- [x] Suggestions on next steps on how to build a more robust infrastructure

## Requested schema
Create curated dataset with only following schema:

| column name         | Description     |
|--------------|-----------|
| time | Timestamp day of recorded earthquake |
| magnitude      | Recorded magnitude of earthquake  |
| latitude      | Latitude of earthquake  |
| longitude      | Longitude of earthquake  |
| place      | Address from where earthquake happened  |
| hased_id      | Hashed ID using all columns of the raw dataset  |
| location      | Name of the extract location  |
| inserted_at      | Timestamp of the extracted data  |

> Additional columns: hased_id, location, inserted_at were added to enrich the dataset further.

# Description
The task is to create a data pipeline that extracts data from United States Geological Survey ([USGS](https://earthquake.usgs.gov/fdsnws/event/1/)) and places it in BigQuery with a defined schema.

About that data:
> The USGS monitors and reports on earthquakes, assesses earthquake impacts and hazards, and conducts targeted research on the causes and effects of earthquakes. We undertake these activities as part of the larger National Earthquake Hazards Reduction Program (NEHRP), a four-agency partnership established by Congress.

This project will find all recorded earthquakes within 500 km of each of the pleo.io offices for the year to date and store the data in a target data warehouse, BigQuery.

<img width="983" alt="image" src="https://github.com/user-attachments/assets/f30f07e5-f921-4e15-a236-685285b1da26">

### Additional information
* [Follow this link](https://docs.google.com/document/d/1xJ-x-0p4zXMwFO3c76kQdt0kvUdWElFVmLnPqXpBJm8/edit) to find further details about task.
* Data [source schema](https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php)
* [Link to architecture](https://miro.com/app/board/uXjVK_LvEq0=/) and notes

## Challenges faced
The main challenge encountered was handling data types for BigQuery. The warehouse requires specific data types, and it will not accept any data that does not conform to these requirements. This limitation posed a significant challenge. However, BigQuery also offers several advantages, such as:

* **Scalability**: Capable of handling large volumes of data efficiently.
* **Performance**: Optimised for fast querying and data processing.
* **Integration**: Seamlessly integrates with various data sources and tools.
* **Accessibility**: Integrations to the Google stack, make it easy to analyze the data via Gsheet or Google Data Studio.

Despite the data type constraints, BigQuery's strengths in these areas proved beneficial for the project.

## Learnings
- **Unit testing and mocking**: Gained proficiency in using unittest and the mock module.
- **Working with GCP BigQuery**:
  - Creating & managing projects and datasets: Learned to create and manage BigQuery projects and datasets.
  - Managing service accounts and secrets: Understood how to handle service accounts and secrets securely.
  - Creating logical logging mechanisms: Developed effective logging mechanisms for debugging.
- **Packaging for deployment**: Learned to package projects for deployment using Docker and Makefile.
- **Working with public APIs**: Acquired skills in handling public APIs, specifically making HTTPS requests.
- **Reusable functions and documentation**: Created reusable functions and wrote proper docstrings following the [PEP 8 style guide](https://peps.python.org/pep-0008).
- **Managing dependencies**: Properly utilised and implemented the requirements.txt file.
- **Virtual environments**: Understood the importance of creating and handling Python virtual environments.
- **Folder hierarchy**: Learned to structure project folders correctly.
- **ETL pipeline best practices**:
  - Created a raw layer for initial data ingestion.
  - Transformed and placed data in a curated layer.
  - Exposed the data to the landing model for consumption.
- **Understanding data lifecycle**:
  - Recognised the importance of retaining raw data for replayability.
  - Understood the need for generalized curation to support multi-purpose downstream usage.
 
# Suggestions for next steps
While this project is fully deployable, there are several areas where enhancements can be made:

1. Automatic scheduling:
    - Currently, the project lacks the capability to be triggered automatically once a week. This is an intended limitation, but with some tweaks, it can be deployed in an Airflow instance or a Kubernetes cluster with minimal effort.
    - The structure of the app.py file follows a similar pattern to an Airflow DAG, indicating that integration with Airflow for scheduling can be achieved seamlessly.
2. User interaction:
    - Improve the app.py file to allow users to add additional addresses dynamically, providing a more interactive and user-friendly experience.
3. Secure handling of secrets:
    - At present, the developer must manually create secrets via the Service Account IAM & Admin function.
    - Enhance security by placing secrets in a secret vault and retrieving them from the script. This approach ensures a more secure and manageable way of handling sensitive information.

By incorporating these improvements, the project's robustness, user-friendliness, and security can be significantly enhanced.

# How to install
The following section will run you through on how to deploy locally with the Dockerfile and Makefile.

## Prerequisites
1. Create a project for this app in BigQuery.
2. In the newly created project, create the datasets: `raw_data` and `curated_data` in BigQuery. Specifically use this naming convention or update the `app.py` correspondingly.
3. Create a service account in the newly created project. This [tutorial](https://www.howtogeek.com/devops/how-to-create-and-use-service-accounts-in-google-cloud-platform/) is helpful in case of doubt.
4. Create keys for the service account and hold them in a safe place until the next step to run the project.

## Run the project
1. Clone the repository.
2. In the app.py update the "BigQuery parameters" as per the ones set by you.
3. Place the keys of the service account in the root directory and rename the keys to `bigquery-project-earthquake-secrets.json`
4. Run the Makefile with:
```
make prod
```
Now the project will build the Docker image and start.

In case you already have built the image or just want to re-run the container without building the image from scratch, use the command:
```
make run
```

# Run tests
Find the tests you want to run and call them with the function
```
python -m unittest tests/{file_name.py}
```
# Technologies used
The following technologies were utilized to implement the project:
* **Python**: Chosen for its versatility, extensive community, and robust support.
* **GeoPy**: Employed for extracting coordinates from addresses.
* **BigQuery**: Selected for being the most accessible and easy-to-deploy cloud data warehouse.
* **Pandas**: Utilised for structuring and cleaning data efficiently.
* **pandas-gbq**: Leveraged to upload Pandas DataFrames to BigQuery.
* **requests**: Utilised to access the API via HTTPS.
* **logging**: To log all required actions.
* **Black**: For better formatting.
