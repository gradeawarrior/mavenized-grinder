Mavenized-Grinder
=================

This is an example Java project for running [The Grinder](http://grinder.sourceforge.net) Java load testing framework using Maven. The added benefit of developing your Grinder load testing scripts this way is that it follows all the great conventions of packaging and executing your Java project using Maven. This in turn also makes it trivial to incorporate into Jenkins and generating automated reports (Jenkins plugin required).

_**NOTE:** All [Grinder](http://grinder.sourceforge.net) features are supported, which includes load testing RESTful webservices to simulating webtraffic load to a website. Please review all features on [The Grinder](http://grinder.sourceforge.net) project website. Modifications can be made under `scripts/src/main/resources`_

# Prerequisites

* Java 6+
* Maven 3.0.2+

# Configuration

All test configurations can be modified at scripts/pom.xml under the properties tag.
Here, all performance and test specific information can be modified that controls
things such as number of threads, number of runs, and number of processes.

These properties in turn manage three configuration files:

1. _grinder.properties_	 - Contains grinder specific configs (e.g. number of processes and threads)
2. _application.properties_ - Application and test specific information

# Steps to run performance tests

* All commands are assumed to be run at the root level of the performance test directory
* Make sure you clean up using `mvn clean`
* All Commands are controled via a `test.command` parameter. The following are
currently supported:

		Usage: mvn test -Dtest.command=<COMMAND>

   		Examples:

		## Basic tests
		mvn test -Dtest.command=foobar
		mvn test -Dtest.command=example-get
		
		## Specifying a different URL
		mvn test -Dtest.command=example-get -Dtest.url=http://localhost:8080/
		
		## Executing 10 concurrent connections 10x using processes
		mvn test -Dtest.command=example-get -Dtest.url=http://localhost:8080/ -Dgrinder.threads=1 -Dgrinder.processes=10 -Dgrinder.runs=10
		## Executing 10 concurrent connections 10x using threads
		mvn test -Dtest.command=example-get -Dtest.url=http://localhost:8080/ -Dgrinder.threads=10 -Dgrinder.processes=1 -Dgrinder.runs=10

	    COMMAND			DESCRIPTION
	    =======			===========
	    example-get		Runs an example GET request against what is configured in scripts/pom.xml file

	    my-test-1		Runs foobar test

	    my-test-2	    Runs helloworld test

	    foobar			(Default) Sample test that prints foobar

	    helloworld		Sample test that prints hello world


References
==========


* **Grinder Home:** http://grinder.sourceforge.net/
* **Grinder Download:** http://sourceforge.net/projects/grinder