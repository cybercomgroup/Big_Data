/**
 * Created by Eren on 2017-03-01.
 * HOWTO:
 * TO INSTALL LIBS: http://stackoverflow.com/questions/36385398/java-hdf5-library-install
 *
 * Add path as args[0] to the m5 files, dont take too many though!
 *
 *
 */

import ncsa.hdf.hdf5lib.H5;
import ncsa.hdf.hdf5lib.HDF5Constants;
import ncsa.hdf.object.h5.H5File;

import javax.swing.filechooser.FileNameExtensionFilter;
import java.io.File;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {

    public static  ArrayList<File> listf(String directoryName) {
        File directory = new File(directoryName);

        ArrayList<File> resultList = new ArrayList<File>();

        // get all the files from a directory
        File[] fList = directory.listFiles();
        resultList.addAll(Arrays.asList(fList));
        for (File file : fList) {
             if (file.isDirectory()) {
                resultList.addAll(listf(file.getAbsolutePath()));
            }
        }
        //System.out.println(fList);
        return resultList;
    }



    public static void main(String[] args) {

        String path = args[0];
        ArrayList<File> fileList = listf(path);

        if (fileList == null) return;

        System.out.println("Amount of files: " + fileList.size());
        for ( File f : fileList ) { //Do whatever for each found file
            String extension;
            try{
                extension = f.getName().substring(f.getName().lastIndexOf(".") + 1);
            }catch (Exception e){
                extension = "";
            }

            if(extension.compareTo("h5") == 0){ //Filetype is correct, do stuff
                H5File song = hdf5_getters.hdf5_open_readonly(f.getPath());
                try{

                    System.out.println("Lenght of the song " + hdf5_getters.get_title(song) + ": " + hdf5_getters.get_duration(song));
                }catch (Exception e){
                    e.printStackTrace();
                    System.out.println("Couldnt reach file: " + song.getPath());
                }

                hdf5_getters.hdf5_close(song);
            }

        }

        System.out.println("Amount of files: " + fileList.size());

    }

}
