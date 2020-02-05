import java.awt.BorderLayout;
import java.awt.CardLayout;
import java.awt.EventQueue;
import java.awt.FlowLayout;
import java.awt.HeadlessException;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import java.awt.Color;

@SuppressWarnings("serial")
public class SlideShow extends JFrame {

	//Declare Variables
	private JPanel slidePane;
	private JPanel textPane;
	private JPanel buttonPane;
	private CardLayout card;
	private CardLayout cardText;
	private JButton btnPrev;
	private JButton btnNext;
	private JLabel lblSlide;
	private JLabel lblTextArea;

	//
	//Create the slide show application
	//
	public SlideShow() throws HeadlessException {
		initComponent();
	}

	//
	//Initialize the contents of the frame
	//
	private void initComponent() {
		//Initialize variables to empty objects
		card = new CardLayout();
		cardText = new CardLayout();
		slidePane = new JPanel();
		textPane = new JPanel();
		textPane.setBackground(Color.YELLOW);
		textPane.setBounds(5, 510, 820, 60);
		textPane.setVisible(true);
		buttonPane = new JPanel();
		btnPrev = new JButton();
		btnNext = new JButton();
		lblSlide = new JLabel();
		lblTextArea = new JLabel();

		//Setup frame attributes
		//Set the size of the frame
		setSize(850, 650);
		setLocationRelativeTo(null);
		
		//Set the title for the slide show
		setTitle("10 Vacation Destinations in 2020 - Relax and Enjoy");
		getContentPane().setLayout(new BorderLayout(10, 50));
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		//Set the layouts for the panels
		slidePane.setLayout(card);
		textPane.setLayout(cardText);
		
		//For loop logic to add each of the 10 slides and text
		for (int i = 1; i <= 10; i++) {
			lblSlide = new JLabel();
			lblTextArea = new JLabel();
			lblSlide.setText(getResizeIcon(i));
			lblTextArea.setText(getTextDescription(i));
			slidePane.add(lblSlide, "card" + i);
			textPane.add(lblTextArea, "cardText" + i);
		}

		//Set the position of the slidePane
		getContentPane().add(slidePane, BorderLayout.CENTER);
		
		//Set the position of the textPane
		getContentPane().add(textPane, BorderLayout.SOUTH);

		buttonPane.setLayout(new FlowLayout(FlowLayout.CENTER, 20, 10));

		//Set the label for the previous button
		btnPrev.setText("Previous");
		btnPrev.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				goPrevious();
			}
		});
		
		//Add the previous button to the pane
		buttonPane.add(btnPrev);

		//Set the label for the next button
		btnNext.setText("Next");
		btnNext.addActionListener(new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent e) {
				goNext();
			}
		});
		
		//Add the next button to the pane
		buttonPane.add(btnNext);

		getContentPane().add(buttonPane, BorderLayout.SOUTH);
	}

	//
	//Set the functionality for the previous button
	//
	private void goPrevious() {
		card.previous(slidePane);
		cardText.previous(textPane);
	}
	
	//
	//Set the functionality for the next button
	//
	private void goNext() {
		card.next(slidePane);
		cardText.next(textPane);
	}

	//
	//Method to get the images and display them within a panel
	//
	private String getResizeIcon(int i) {
		String image = ""; 
		if (i==1){
			image = "<html><body><img width= '830' height='500' src='" + getClass().getResource("/resources/copenhagen_denmark.jpg") + "'</body></html>";
		} else if (i==2){
			image = "<html><body><img width= '800' height='500' src='" + getClass().getResource("/resources/dominica.jpg") + "'</body></html>";
		} else if (i==3){
			image = "<html><body><img width= '800' height='500' src='" + getClass().getResource("/resources/estonia.jpg") + "'</body></html>";
		} else if (i==4){
			image = "<html><body><img width= '800' height='500' src='" + getClass().getResource("/resources/galway_ireland.jpg") + "'</body></html>";
		} else if (i==5){
			image = "<html><body><img width= '800' height='500' src='" + getClass().getResource("/resources/jamaica.jpg") + "'</body></html>";
		} else if (i==6){
			image = "<html><body><img width= '800' height='500' src='" + getClass().getResource("/resources/kyushu_japan.jpg") + "'</body></html>";
		} else if (i==7){
			image = "<html><body><img width= '800' height='500' src='" + getClass().getResource("/resources/new_caldonia_france.jpg") + "'</body></html>";
		} else if (i==8){
			image = "<html><body><img width= '800' height='500' src='" + getClass().getResource("/resources/st_petersburg_russia.jpg") + "'</body></html>";
		} else if (i==9){
			image = "<html><body><img width= '800' height='500' src='" + getClass().getResource("/resources/the_dead_sea.jpg") + "'</body></html>";
		} else if (i==10){
			image = "<html><body><img width= '800' height='500' src='" + getClass().getResource("/resources/vancouver_island_british_columbia.jpg") + "'</body></html>";
		}
		
		return image;
	}
	
	//
	//Method to get the text values and display them within a panel
	//
	private String getTextDescription(int i) {
		String text = ""; 
		if (i==1){
			text = "<html><body><font size='5'>Copenhagen.</font> <br>Characterized by its canals and known as the happiest city in the world. <br>https://www.visitcopenhagen.com/</body></html>";
		} else if (i==2){
			text = "<html><body><font size='5'>Dominica.</font> <br>Largely covered by rainforest and home to the 2nd largest hot spring, Boiling Lake. <br>https://discoverdominica.com/en/home/</body></html>";
		} else if (i==3){
			text = "<html><body><font size='5'>Estoria.</font> <br>The northernmost of the three Baltic states and home to the historic medieval town Tallinn. <br>https://www.visitestonia.com/en/</body></html>";
		} else if (i==4){
			text = "<html><body><font size='5'>Galway.</font> <br>Renowned for its vibrant festivals, hosting on average 122 per year. <br>https://www.galwaytourism.ie/</body></html>";
		} else if (i==5){
			text = "<html><body><font size='5'>Jamaica.</font> <br>Famous for reggae music, white sand beaches, and a warm, sunny climate all year long. <br>https://www.visitjamaica.com/</body></html>";
		} else if (i==6){
			text = "<html><body><font size='5'>Kyushu.</font> <br>Home to Mount Aso, the world's largest active volcano. <br>https://www.welcomekyushu.com/</body></html>";
		} else if (i==7){
			text = "<html><body><font size='5'>New Caledonia.</font> <br>Surrounded by a barrier reef and one of the largest tropical lagoons. <br>https://www.newcaledonia.travel/en/</body></html>";
		} else if (i==8){
			text = "<html><body><font size='5'>Saint Petersburg.</font> <br>The second largest city in Russia is home to historical churches, palaces, and museums. <br>http://www.saint-petersburg.com/</body></html>";
		} else if (i==9){
			text = "<html><body><font size='5'>The Dead Sea.</font> <br>Known for being one of the saltiest bodies of water in the world and devoid of any fish and aquatic plants. <br>https://www.touristisrael.com/dead-sea/289/</body></html>";
		} else if (i==10){
			text = "<html><body><font size='5'>Vancouver Island.</font> <br>Famous for its lakes, waterfalls, and mountains with glaciers. <br>https://vancouverisland.travel/</body></html>";
		}
		
		return text;
	}

	//
	//Launch the application
	//
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {

			@Override
			public void run() {
				SlideShow ss = new SlideShow();
				ss.setVisible(true);
			}
		});
	}
}