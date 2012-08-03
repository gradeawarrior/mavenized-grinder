from net.grinder.script.Grinder import grinder
from net.grinder.script import Test
from net.grinder.plugin.http import HTTPRequest
from com.proofpoint.grinder import GrinderUtil
from HTTPClient import NVPair
from java.util import Properties
from java.util import UUID
from ch.qos.logback.classic import Logger
from  org.apache.commons.codec.digest import  DigestUtils

log = grinder.logger.output
out = grinder.logger.LOG

grinderUtil = GrinderUtil.getSingleton()
configProperties = grinderUtil.getApplicationProperties()

testCommand = grinderUtil.getApplicationProperty("test.command")

url = configProperties.getProperty("url")
testWrap = Test(1, "General Tests")
wrappedRequest = testWrap.wrap(HTTPRequest())

tests = { "Index Page" :Test(1, "Index Page") }

execCounter = 0

print "testCommand=%s" % (testCommand)

class TestRunner:
    def __call__(self):
        print "testCommand=%s" % (testCommand)
        if testCommand == "file-upload":
            uploadFile()
        elif testCommand == "share-event":
            test1()
        elif testCommand == "message-summary":
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
