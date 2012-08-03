package com.proofpoint.grinder;

import HTTPClient.HTTPResponse;
import HTTPClient.NVPair;
import ch.qos.logback.classic.Level;
import ch.qos.logback.classic.Logger;
import com.google.common.base.Charsets;
import com.google.common.io.Files;
import com.google.common.io.InputSupplier;
import com.google.common.io.Resources;
import net.grinder.plugin.http.HTTPPluginControl;
import net.grinder.plugin.http.HTTPRequest;
import net.grinder.plugin.http.HTTPUtilities;
import org.slf4j.LoggerFactory;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Properties;
import java.util.Random;


/* This class is an utility class for running Grinder tests
*  The main grinder script that uses this one is tests.py
*/
public class GrinderUtil
{
    ch.qos.logback.classic.Logger logger = (ch.qos.logback.classic.Logger) LoggerFactory.getLogger(GrinderUtil.class);
    private static GrinderUtil ref;
    public static final int DEFAULT_BYTE_ARRAY_LENGTH = 1000000;
    private static final int DEBUG_DISPLAY_LIMIT = 20;

    private final Random randomGenerator;
    private final Properties grinderProperties = new Properties();
    private final Properties applicationProperties = new Properties();

    // all the following files are required before running a test
    private GrinderUtil()
    {
        randomGenerator = new Random((new Date()).getTime());
        try {
            loadPropertiesByName("grinder.properties", grinderProperties);
            loadPropertiesByName("application.properties", applicationProperties);
        }
        catch (IOException ioe) {
            logger.error("Required files must exist. " + ioe.toString());
            System.exit(1);
        }

        int maxRun = Integer.valueOf(grinderProperties.getProperty("grinder.runs"));
        if (maxRun < DEBUG_DISPLAY_LIMIT) {
            logger.setLevel(Level.DEBUG);
        }
        else {
            logger.setLevel(Level.INFO);
        }
    }

    public static synchronized GrinderUtil getSingleton()
    {
        if (ref == null) {
            ref = new GrinderUtil();
        }
        return ref;
    }

    public Properties getApplicationProperties()
    {
        return applicationProperties;
    }

    public String getApplicationProperty(String name)
    {
        return applicationProperties.getProperty(name);
    }

    public Logger getLogger()
    {
        return logger;
    }

    public void loadPropertiesByName(String fileName, Properties properties)
            throws IOException
    {
        String filePath = Resources.getResource(fileName).getFile();
        File propFile = new File(filePath);
        InputSupplier<FileInputStream> inputStreamInputSupplier = Files.newInputStreamSupplier(propFile);
        properties.load(inputStreamInputSupplier.getInput());
    }

    public NVPair createAuthHeader(String user, String password)
    {

        HTTPUtilities httpUtilities = HTTPPluginControl.getHTTPUtilities();
        NVPair authNV = httpUtilities.basicAuthorizationHeader(user, password);
        return authNV;
    }

    //generate bounded random array
    public byte[] getRandomByteArray(int length)
    {

        int byteLength = length;
        if (length <= 0) {
            byteLength = randomGenerator.nextInt(DEFAULT_BYTE_ARRAY_LENGTH) + 1;
        }

        byte[] randomByteArray = new byte[byteLength];
        randomGenerator.nextBytes(randomByteArray);
        return randomByteArray;
    }
}
