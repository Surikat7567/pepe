import javax.sound.sampled.*;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.MalformedURLException;
import java.net.URL;

@SuppressWarnings("SpellCheckingInspection")
public class Main {
    public static void main (String[] args) {
        JFrame wind = getFrame();
        wind.add(new Comp());
    }

    static class Comp extends JComponent{
        @Override
        protected void paintComponent(Graphics g) {
            Graphics2D g2 = (Graphics2D)g;
            try {
                URL url = new URL("https://images.squarespace-cdn.com/content/v1/5bf85ceb9772aeb688fe5f4b/1570296207268-U4NY4ZXJEYNV056X738Q/20190523_202042+-+wm.jpg?format=1000w");
                Image drm_im = new ImageIcon("C:\\pepe-Drums-2\\src\\drm.png").getImage();
                g2.drawImage(drm_im,0,0, 1000, 486, null);
            }catch (MalformedURLException e){
                e.printStackTrace();
            }
        }
    }
    static JFrame getFrame(){
        JFrame wind = new JFrame(){};
        wind.setVisible(true);
        wind.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        wind.setTitle("Drums");
        wind.setBounds(30,20,1000,485);
        //...Button ||hi hat cl|| creating part......................
        JButton button = new JButton("Hihat");
        button.setBounds(181,130,70,30);
        button.addActionListener(e -> {
            try {
                File soundFile = new File("C:\\pepe-Drums-2\\src\\hihat_cl.wav"); //Звуковий файл

                AudioInputStream ais = AudioSystem.getAudioInputStream(soundFile);

                Clip clip = AudioSystem.getClip();
                clip.open(ais);
                clip.setFramePosition(0);
                clip.start();
                // поставити в цикл для відновлення вікна wind.setBounds(30,20,1000,485);
            } catch (IOException | UnsupportedAudioFileException | LineUnavailableException exc) {
                exc.printStackTrace();
            }// catch (InterruptedException exc) {}
        });

        //...............................................
        //...Button ||c|| creating part......................
        JButton crashbutton = new JButton("crash");
        crashbutton.setBounds(241,40,70,30);
        crashbutton.addActionListener(e -> {
            try {
                File csoundFile = new File("C:\\pepe-Drums-2\\src\\crash.wav"); //Звуковий файл

                AudioInputStream cais = AudioSystem.getAudioInputStream(csoundFile);

                Clip clip2 = AudioSystem.getClip();
                clip2.open(cais);
                clip2.setFramePosition(0);
                clip2.start();
            } catch (IOException | UnsupportedAudioFileException | LineUnavailableException exc) {
                exc.printStackTrace();
            }
        });
        //...Button ||Ride crimbal|| creating part......................
        JButton rbutton = new JButton("ride");
        rbutton.setBounds(541,80,70,30);
        rbutton.addActionListener(e -> {
            try {
                File rsoundFile = new File("C:\\pepe-Drums-2\\src\\R.wav"); //Звуковий файл

                AudioInputStream rais = AudioSystem.getAudioInputStream(rsoundFile);

                Clip clip3 = AudioSystem.getClip();
                clip3.open(rais);
                clip3.setFramePosition(0);
                clip3.start();
            } catch (IOException | UnsupportedAudioFileException | LineUnavailableException exc) {
                exc.printStackTrace();
            }
        });
        //...Button ||Ride2 crimbal|| creating part......................
        JButton r2button = new JButton("Ride");
        r2button.setBounds(721,70,70,30);
        r2button.addActionListener(e -> {
            try {
                File r2soundFile = new File("C:\\pepe-Drums-2\\src\\RR.wav"); //Звуковий файл

                AudioInputStream r2ais = AudioSystem.getAudioInputStream(r2soundFile);

                Clip clip4 = AudioSystem.getClip();
                clip4.open(r2ais);
                clip4.setFramePosition(0);
                clip4.start();
            } catch (IOException | UnsupportedAudioFileException | LineUnavailableException exc) {
                exc.printStackTrace();
            }
        });
        //...Button ||Snare|| creating part......................
        JButton sbutton = new JButton("Snare");
        sbutton.setBounds(333,210,70,30);
        sbutton.addActionListener(e -> {
            try {
                File SsoundFile = new File("C:\\pepe-Drums-2\\src\\SSSnare.wav"); //Звуковий файл

                AudioInputStream sais = AudioSystem.getAudioInputStream(SsoundFile);

                Clip clipS = AudioSystem.getClip();
                clipS.open(sais);
                clipS.setFramePosition(0);
                clipS.start();
            } catch (IOException | UnsupportedAudioFileException | LineUnavailableException exc) {
                exc.printStackTrace();
            }
        });
        //...Button ||Htigh Tom|| creating part......................
        JButton Htbutton = new JButton("Hi-Tom");
        Htbutton.setBounds(330,123,75,30);
        Htbutton.addActionListener(e -> {
            try {
                File HsoundFile = new File("C:\\pepe-Drums-2\\src\\HiTom.wav"); //Звуковий файл

                AudioInputStream Htais = AudioSystem.getAudioInputStream(HsoundFile);

                Clip clipH = AudioSystem.getClip();
                clipH.open(Htais);
                clipH.setFramePosition(0);
                clipH.start();
            } catch (IOException | UnsupportedAudioFileException | LineUnavailableException exc) {
                exc.printStackTrace();
            }
        });
        //...Button ||High Tom|| creating part......................
        JButton Ltbutton = new JButton("L-Tom");
        Ltbutton.setBounds(560,222,70,30);
        Ltbutton.addActionListener(e -> {
            try {
                File LtsoundFile = new File("C:\\pepe-Drums-2\\src\\LTom.wav"); //Звуковий файл

                AudioInputStream Ltais = AudioSystem.getAudioInputStream(LtsoundFile);

                Clip clipLt = AudioSystem.getClip();
                clipLt.open(Ltais);
                clipLt.setFramePosition(0);
                clipLt.start();
            } catch (IOException | UnsupportedAudioFileException | LineUnavailableException exc) {
                exc.printStackTrace();
            }
        });
        //...Button ||Floor Tom|| creating part......................
        JButton Ftbutton = new JButton("F-Tom");
        Ftbutton.setBounds(650,300,70,30);
        Ftbutton.addActionListener(e -> {
            try {
                File FtsoundFile = new File("C:\\pepe-Drums-2\\src\\FTom.wav"); //Звуковий файл

                AudioInputStream Ftais = AudioSystem.getAudioInputStream(FtsoundFile);

                Clip clipFt = AudioSystem.getClip();
                clipFt.open(Ftais);
                clipFt.setFramePosition(0);
                clipFt.start();
            } catch (IOException | UnsupportedAudioFileException | LineUnavailableException exc) {
                exc.printStackTrace();
            }
        });
        //...Button ||Bass|| creating part......................
        JButton bassbutton = new JButton("Bass");
        bassbutton.setBounds(448,300,70,30);
        bassbutton.addActionListener(e -> {
            try {
                File bassSoundFile = new File("C:\\pepe-Drums-2\\src\\Bass.wav"); //Звуковий файл

                AudioInputStream bass = AudioSystem.getAudioInputStream(bassSoundFile);

                Clip clipB = AudioSystem.getClip();
                clipB.open(bass);
                clipB.setFramePosition(0);
                clipB.start();
            } catch (IOException | UnsupportedAudioFileException | LineUnavailableException exc) {
                exc.printStackTrace();
            }
        });

        wind.add(r2button);
        wind.add(button);
        wind.add(Htbutton);
        wind.add(sbutton);
        wind.add(crashbutton);
        wind.add(rbutton);
        wind.add(Ltbutton);
        wind.add(Ftbutton);
        wind.add(bassbutton);
        wind.setTitle("drm");

        return wind;
    }


}