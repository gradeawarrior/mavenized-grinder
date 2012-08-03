package com.proofpoint.grinder;


import org.testng.annotations.Test;

import java.io.File;
import java.io.IOException;
import java.util.List;
import java.util.Properties;

import static org.testng.Assert.assertEquals;

public class TestPerfUtil
{
    private final GrinderUtil grinderUtil = GrinderUtil.getSingleton();

    @Test
    public void testLoadApplicationConfig()
            throws IOException
    {
        Properties props = grinderUtil.getApplicationProperties();

        assertEquals(props.getProperty("grinder.processes"), "1");
        assertEquals(props.getProperty("grinder.runs"), "10");
        assertEquals(props.getProperty("grinder.threads"), "1");
        assertEquals(props.getProperty("grinder.script"), "tests.py");
        assertEquals(props.getProperty("grinder.logProcessStreams"), "false");
        assertEquals(props.getProperty("test.command"), "foobar");
        assertEquals(props.getProperty("test.url"), "http://www.example.com");
    }

    @Test
    public void testGetRandomByteArray()
    {
        for (int i = 0; i < 10; i++) {
            int length = (int) (Math.random() * GrinderUtil.DEFAULT_BYTE_ARRAY_LENGTH + 1);
            grinderUtil.getLogger().debug("required byte length="+length);
            byte[] bytes = grinderUtil.getRandomByteArray(length);
            assertEquals(bytes.length, length);
        }
    }
}
