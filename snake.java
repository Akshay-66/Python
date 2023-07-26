import java.awt.Color;
import java.awt.Dimension;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.util.Random;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class SnakeGame extends JPanel implements KeyListener, Runnable {

    private static final int WIDTH = 600;
    private static final int HEIGHT = 600;
    private static final int UNIT_SIZE = 20;
    private static final int GAME_UNITS = (WIDTH * HEIGHT) / (UNIT_SIZE * UNIT_SIZE);
    private static final int DELAY = 75;

    private final int[] xs = new int[GAME_UNITS];
    private final int[] ys = new int[GAME_UNITS];
    private int bodyParts = 6;
    private int appleEaten;
    private int appleX;
    private int appleY;
    private char direction = 'R';
    private boolean running = false;

    private final Random random;
    private final Font scoreFont;

    public SnakeGame() {
        random = new Random();
        scoreFont = new Font("Arial", Font.PLAIN, 20);
        setPreferredSize(new Dimension(WIDTH, HEIGHT));
        setBackground(Color.WHITE);
        setFocusable(true);
        addKeyListener(this);
        startGame();
    }

    private void startGame() {
        running = true;
        spawnApple();
        xs[0] = 0;
        ys[0] = 0;
        bodyParts = 6;
        appleEaten = 0;
        direction = 'R';

        Thread thread = new Thread(this);
        thread.start();
    }

    private void spawnApple() {
        appleX = random.nextInt((WIDTH / UNIT_SIZE)) * UNIT_SIZE;
        appleY = random.nextInt((HEIGHT / UNIT_SIZE)) * UNIT_SIZE;
    }

    private void move() {
        for (int i = bodyParts; i > 0; i--) {
            xs[i] = xs[i - 1];
            ys[i] = ys[i - 1];
        }

        switch (direction) {
            case 'U':
                ys[0] = ys[0] - UNIT_SIZE;
                break;
            case 'D':
                ys[0] = ys[0] + UNIT_SIZE;
                break;
            case 'L':
                xs[0] = xs[0] - UNIT_SIZE;
                break;
            case 'R':
                xs[0] = xs[0] + UNIT_SIZE;
                break;
        }
    }

    private void checkApple() {
        if (xs[0] == appleX && ys[0] == appleY) {
            bodyParts++;
            appleEaten++;
            spawnApple();
        }
    }

    private void checkCollisions() {
        // Check if head collides with body
        for (int i = bodyParts; i > 0; i--) {
            if (xs[0] == xs[i] && ys[0] == ys[i]) {
                running = false;
                break;
            }
        }

        // Check if head touches boundaries
        if (xs[0] < 0 || xs[0] >= WIDTH || ys[0] < 0 || ys[0] >= HEIGHT) {
            running = false;
        }

        if (!running) {
            gameOver();
        }
    }

    private void gameOver() {
        // Handle game over logic
        System.exit(0);
    }

    private void draw(Graphics g) {
        if (running) {
            // Draw snake
            for (int i = 0;i < bodyParts; i++) {
                            g.setColor(Color.RED);
                            g.fillRect(xs[i], ys[i], UNIT_SIZE, UNIT_SIZE);
                        }
            
                        // Draw apple
                        g.setColor(Color.GREEN);
                        g.fillOval(appleX, appleY, UNIT_SIZE, UNIT_SIZE);
            
                        // Draw score
                        g.setColor(Color.BLACK);
                        g.setFont(scoreFont);
                        g.drawString("Score: " + appleEaten, 10, 20);
                    } else {
                        gameOverScreen(g);
                    }
                }
            
                private void gameOverScreen(Graphics g) {
                    // Game over screen
                    g.setColor(Color.BLACK);
                    g.setFont(new Font("Arial", Font.BOLD, 40));
                    g.drawString("Game Over", WIDTH / 2 - 110, HEIGHT / 2 - 30);
                    g.setFont(scoreFont);
                    g.drawString("Score: " + appleEaten, WIDTH / 2 - 50, HEIGHT / 2 + 10);
                }
            
                @Override
                public void keyPressed(KeyEvent e) {
                    int key = e.getKeyCode();
                    if (key == KeyEvent.VK_LEFT && direction != 'R') {
                        direction = 'L';
                    } else if (key == KeyEvent.VK_RIGHT && direction != 'L') {
                        direction = 'R';
                    } else if (key == KeyEvent.VK_UP && direction != 'D') {
                        direction = 'U';
                    } else if (key == KeyEvent.VK_DOWN && direction != 'U') {
                        direction = 'D';
                    }
                }
            
                @Override
                public void keyTyped(KeyEvent e) {
                }
            
                @Override
                public void keyReleased(KeyEvent e) {
                }
            
                @Override
                public void run() {
                    while (running) {
                        move();
                        checkApple();
                        checkCollisions();
                        repaint();
            
                        try {
                            Thread.sleep(DELAY);
                        } catch (InterruptedException e) {
                            e.printStackTrace();
                        }
                    }
                }
            
                public static void main(String[] args) {
                    JFrame frame = new JFrame("Snake");
                    SnakeGame game = new SnakeGame();
                    frame.add(game);
                    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                    frame.setResizable(false);
                    frame.pack();
                    frame.setLocationRelativeTo(null);
                    frame.setVisible(true);
                }
            }
            