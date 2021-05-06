package bachelor2021.fileconverter;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class FileConverter {

    public static HashMap<String, String> mapGuidFilenames(String filname) {
        HashMap<String, String> fileMapper = new HashMap<>();

        try(BufferedReader bufferedReader = new BufferedReader(new FileReader(filname))) {
            String line;
            while ((line = bufferedReader.readLine()) != null) {
                String[] splitter = line.split("\t");
                fileMapper.put(splitter[0], splitter[1]);
            }

        } catch (IOException ioe) {
            System.out.println(ioe);
        }

        return fileMapper;
    }

    public static void convertFilename(String filename, HashMap<String, String> fileMapper) {
        HashMap<String, Integer> occurences = new HashMap<>();
        HashMap<String, Boolean> filenameOccurences = new HashMap<>();
        File dir = new File(filename);
        File[] files = dir.listFiles();

        int i = 0;
        assert files != null;
        for (File file : files) {
            i++;
            String name = file.getName().toUpperCase();

            if (fileMapper.containsKey(name)) {
                String newName = fileMapper.get(name);
                /*if (!occurences.containsKey(newName))
                    occurences.put(newName, 1);
                else*/
                /*filenameOccurences.put(newName, false);*/
                occurences.put(newName, occurences.getOrDefault(newName, 0) + 1);

               /* if (occurences.get(newName) > 1) {*/
                    String[] newNameTemp = newName.split("[.]", 0);
                    newName = newNameTemp[0] + (occurences.get(newName) + 55) +  "." + newNameTemp[1];
                    /*filenameOccurences.put(newName, true);*/
               /* }*/
/*
                if (filenameOccurences.get(newName)) {
                    String[] newNameTemp = newName.split("[.]", 0);
                    newName = newNameTemp[0] + occurences.get(newName) + "a" + "." + newNameTemp[1];
                    filenameOccurences.put(newName, true);
                }
                filenameOccurences.put(newName, true);*/

                String newPath = filename + "\\" + newName;
                file.renameTo(new File(newPath));

                System.out.println(name + " renamed to " + newName + " " + i);
            }

        }

        for (Map.Entry<String, Integer> entry : occurences.entrySet()) {
            System.out.println("Occurance: " + entry.getKey() + " - Count: " + entry.getValue());
        }

        /*for (Map.Entry<String, Boolean> entry : filenameOccurences.entrySet()) {
            System.out.println("File occurance: " + entry.getKey() + " - Bool: " + entry.getValue());
        }*/
    }
}
