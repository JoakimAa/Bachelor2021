package bachelor2021.fileconverter;

import java.io.File;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class Main {

    public static void main(String[] args) {
        HashMap<String, String> fileMapper = new HashMap<String, String>();

        fileMapper = FileConverter.mapGuidFilenames("src/data.txt");

        for (Map.Entry<String, String> entry : fileMapper.entrySet()) {
            System.out.println("Guid: " + entry.getKey() + " - Filename: " + entry.getValue());
        }

        String absolutePath = "src/data.AM4140";
        FileConverter.convertFilename(absolutePath, fileMapper);
    }
}
