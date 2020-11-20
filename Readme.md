# News Management System
## Installation Guide
* Clone this [Respositry](https://github.com/svkausthubh/Intellimind)
* Install the following dependencies:(VirtualEnvironment Recommended)
    
    * BeautifulSoup
    * Pymongo
    * Json
    * Concurrent.Features
    * Pandas
    * Newspaper
    * Requests
    * Flask
* The Database used is Mongodb,please connect to the mongob server.

* Provide The Output Directory And The Source File In The "News_Feed.sh".

* Run the following command:
```
sh News_Feed.sh
```
* For the Flask Server Components in the current shell
```
 ./news_server.sh
```
* Different operations of the project are divided into different modules and are named accordingly.

## Routing

### Homepage
* @app.route('/')
* Displays the number of articles extracted from each source.

### Atricles Recieved On Particular Date
* @app.route('Articles/<string:n>')
* provide the date required in the following manner:
```
url/Articles/Date Required
```
### Number Of Articles On A Particular Company
* @app.route('/companies,methods=['GET','POST']')
* Provide the company security code in the following manner(It is a "POST" method):
```
{
    "company":Company Security Code
}


