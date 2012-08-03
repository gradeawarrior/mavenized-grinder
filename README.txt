#################
# Prerequisites #
#################

* Java 6
* Maven 3.0.2+


#################
# Configuration #
#################

All test configurations can be modified at scripts/pom.xml under the properties tag.
Here, all performance and test specific information can be modified that controls
things such as number of threads, number of runs, number of processes, and the
discovery URL.

These properties in turn manage three configuration files:
i) grinder.properties		Contains grinder specific configs (e.g. number of processes and threads)
ii) application.properties	Application and test specific information


##################################
# Steps to run performance tests #
##################################

** All commands are assumed to be run at the root level of the performance test directory

** Make sure you clean up.
mvn clean

** All Commands are controled via a "test.command" parameter. The following are
currently supported:

	Usage: mvn -Dtest.command=<COMMAND> test

    Examples:

        mvn -Dtest.command=foobar test
        mvn -Dtest.command=example-get test

    COMMAND			DESCRIPTION
    =======			===========
    example-get		Runs an example GET request against what is configured in scripts/pom.xml file

    my-test-1		Runs foobar test

    my-test-2	    Runs helloworld test

    foobar			(Default) Sample test that prints foobar

    helloworld		Sample test that prints hello world

##############
# References #
##############

* Grinder Home:
	http://grinder.sourceforge.net/

* Grinder Download:
	http://sourceforge.net/projects/grinder/
