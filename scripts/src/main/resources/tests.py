from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from com.proofpoint.grinder import GrinderUtil
from HTTPClient import NVPair
from java.util import UUID

log = grinder.logger.info
#out = grinder.logger.LOG

grinderUtil = GrinderUtil.getSingleton()
applicationProperties = grinderUtil.getApplicationProperties()

testCommand = applicationProperties.getProperty("test.command")
url = applicationProperties.getProperty("test.url")

grinderUtil = GrinderUtil.getSingleton()
applicationProperties = grinderUtil.getApplicationProperties()

# The default command should be "foobar"
testCommand = applicationProperties.getProperty("test.command")

# The default should be "http://www.example.com/" set in the pom.xml
url = applicationProperties.getProperty("test.url")

testWrap = Test(1, "General Tests")
wrappedRequest = testWrap.wrap(HTTPRequest())

tests = { "Example" :Test(1, "Index Page") }

execCounter = 0

class TestRunner:
    def __call__(self):
        print "testCommand=%s" % (testCommand)
        if testCommand == "example-get":
            getRequest()
        elif testCommand == "my-test-1":
            test1()
        elif testCommand == "my-test-2":
            test1()
        elif testCommand == "foobar":
            test1()
        elif testCommand == "helloworld":
             test2()


def uploadFile():
    fileId = UUID.randomUUID()
    body = "foobar test"
    headers = ()

    putUrl = "%s/v1/file/%s" % (url, fileId)
    grinder.statistics.delayReports = 1
    putWrap = tests["/v1/file"].wrap(HTTPRequest())
    result = putWrap.PUT(putUrl, body, headers)
    
    if(result.statusCode !=200) :
      grinder.statistics.forLastTest.setSuccess(0)

def getRequest():
    grinder.statistics.delayReports = 1
    result = tests["Example"].wrap(HTTPRequest()).GET(url)

    if (result.statusCode != 200) :
        grinder.statistics.forLastTest.setSuccess(0)

def test1 ():
    print "foobar test - Example Service URL:%s - UUID:%s" % (url, UUID.randomUUID())

def test2 ():
    print "hello world test - Example Service URL:%s - UUID:%s" % (url, UUID.randomUUID())

def legacyRequest():
    grinderUtil.loadKeyValsFromStore()
    index = grinderUtil.getRandomIndex()
    key = grinderUtil.getKeyFromKVStore(index)
    sha = grinderUtil.getSha256HexFromKVStore(index)
    headers = (
    grinderUtil.createAuthHeader(),
    NVPair('X-Proofpoint-Content-SHA256', sha),
    NVPair('X-proofpoint-product-tag', productTag),
    NVPair('X-proofpoint-customer-tag', customerTag))

    queryData = ()
    #getUrl = grinderUtil.getUrlWithKey(key)
    #result = wrappedRequest.GET(getUrl, queryData, headers)
    #print "status code =%s" % (result.statusCode)
